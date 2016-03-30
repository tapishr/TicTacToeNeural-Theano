import numpy
import cPickle
import theano
import theano.tensor as T

LEARNING_RATE = 0.09


class HiddenLayer(object):

	def __init__(self, inputVector, n_in = None, n_nodes = None, activation = None, W = None, b = None):

		if W is None:
			
			rng = numpy.random.RandomState(23452)
			n_out = n_nodes
			W_bound = numpy.sqrt(6. / (n_in + n_out))

			W = theano.shared(
				name = 'W_HiddenLayer',
				value = numpy.asarray(
					rng.uniform(
						low = - W_bound,
						high = W_bound,
						size = (n_in, n_out)),
					dtype = theano.config.floatX),
				)
			# if activation == T.nnet.sigmoid :
			# 	W *= 4
		self.W = W
		
		if b is None:
			b = theano.shared(
				name = 'b_HiddenLayer',
				value = numpy.zeros( 
					n_out, 
					dtype = theano.config.floatX))
		self.b = b
		
		self.output = activation (T.dot(inputVector, self.W) + self.b)

		self.params = [self.W, self.b]



class OutputLayerQscore(object) :

	def __init__ (self, inputVector, n_in = None, n_nodes = None, W = None, b = None):
		 
		if W is None:
		 	rng = numpy.random.RandomState(23452)
			n_out = n_nodes
			W_bound = numpy.sqrt(6. / (n_in + n_out))

			W = theano.shared(
				name = 'W_OutputLayer',
				value = numpy.asarray(
					rng.uniform(
						low = - W_bound,
						high = W_bound,
						size = (n_in, n_out)),
					dtype = theano.config.floatX),
				)
		self.W = W

		if b is None:
			b = theano.shared(
				name = 'b_OutputLayer',
				value = numpy.zeros( 
					n_out, 
					dtype = theano.config.floatX))
		self.b = b

		self.output = T.nnet.sigmoid(T.dot(inputVector, W) + b)

		self.params = [self.W, self.b]

	
	def cost(self, y):
		if y.ndim != self.output.ndim:
			raise TypeError(
				'y should have the same shape as self.output',
				('y', y.type, 'self.output', self.output.type)
				)

		return -T.nnet.binary_crossentropy(self.output, y).mean()



class QScoreLearner(object):


	def __init__(self, player_mark, n_nodes = None, n_in = None, file_name = None):

		self.player_mark = player_mark
		self.inputVector = T.dvector('inputVector')
		self.n_nodes = n_nodes
		if file_name is None:
			self.layer0 = HiddenLayer(
				inputVector = self.inputVector,
				n_in = n_in,
				n_nodes = n_nodes,
				activation = T.nnet.sigmoid)
			self.layer1 = OutputLayerQscore(
				inputVector = self.layer0.output,
				n_in = n_nodes,
				n_nodes = 1)
			self.layerParams = self.layer0.params + self.layer1.params
		else :
			self.layerParams = cPickle.load(open(file_name))
			self.layer0 = HiddenLayer(
				inputVector = self.inputVector,
				activation = T.nnet.sigmoid,
				W = self.layerParams[0],
				b = self.layerParams[1])
			self.layer1 = OutputLayerQscore(
				inputVector = self.layer0.output,
				W = self.layerParams[2],
				b = self.layerParams[3])


	def predict(self, input_board):

		prediction_function = theano.function(
			inputs = [self.inputVector],
			outputs = self.layer1.output
		)

		req_index = -1
		max_q_value = -1

		for index, x in numpy.ndenumerate(input_board):

			if x == 0:
				new_board = numpy.copy(input_board)
				new_board[index] = self.player_mark
				q_value = prediction_function(new_board.flatten())
				if q_value > max_q_value:
					max_q_value = q_value
					req_index = index

		return req_index



	def give_reward(self, reward_value, input_board):
		y = T.lvector('y')
		cost = self.layer1.cost(y)
		grads = T.grad(cost, self.layerParams)
		updates = [
				(param_i, param_i - LEARNING_RATE * grad_i) 
				for param_i, grad_i in zip(self.layerParams, grads)
				]
		y_value = numpy.asarray([reward_value])
		training_function = theano.function(
					inputs = [self.inputVector],
					outputs = self.layer1.output,
					updates = updates,
					givens={
						y:y_value
					}
				)
		return training_function(input_board.flatten())


	def save_model(self):
		nameOfFile = 'player' + str(self.player_mark) + 'QlearnerModelWithNodes' + str(self.n_nodes)
		with open(nameOfFile, 'w') as f:
                        cPickle.dump(self.layerParams, f)

	