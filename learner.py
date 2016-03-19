import numpy
import theano
import theano.tensor as T
from theano.tensor.nnet import conv

class DeepLearner:

	LEARNING_RATE = 0.8

	def __init__(self, init_params = None):

		self.input_board = T.dmatrix('input_board')
		
		rng = numpy.random.RandomState(23455)
		filter_shape = (1,1,5,5)
		image_shape = (1,1,10,10)
		n_in_layer0 = numpy.prod(filter_shape[1:])
		n_out_layer0 = filter_shape[0] * numpy.prod(filter_shape[2:])
		W_bound_layer0 = numpy.sqrt(6. / (n_in_layer0 + n_out_layer0))	
		if init_params is None:
			W_layer0 = theano.shared(
				numpy.asarray(
					rng.uniform(low = -W_bound_layer0, high = W_bound_layer0, size = filter_shape),
					dtype = theano.config.floatX),
				borrow = True)
			b_value_layer0 = numpy.zeros((filter_shape[0],), dtype = theano.config.floatX)
			b_layer0 = theano.shared(value = b_value_layer0, borrow = True)

			n_in_layer1 = 36
			n_out_layer1 = 50
			
			W_bound_layer1 = numpy.sqrt(6. / (n_in_layer1 + n_out_layer1))
			W_layer1 = theano.shared(
					numpy.asarray(
						rng.uniform(
							low = -W_bound_layer1, 
							high = W_bound_layer1, 
							size = (n_in_layer1, n_out_layer1)),
						dtype = theano.config.floatX),
					borrow = True)
			b_value_layer1 = numpy.zeros((n_out_layer1,), dtype = theano.config.floatX)
			b_layer1 = theano.shared(value = b_value_layer1, borrow = True)
			n_in_layer2 = n_out_layer1
			n_out_layer2 = 1
			W_bound_layer2 = numpy.sqrt(6. / (n_in_layer2 + n_out_layer2))
			W_layer2 = theano.shared(
					numpy.asarray(
						rng.uniform(
							low = -W_bound_layer2, 
							high = W_bound_layer2, 
							size = (n_in_layer2, n_out_layer2)),
						dtype = theano.config.floatX),
					borrow = True)
			b_value_layer2 = numpy.zeros((n_out_layer2,), dtype = theano.config.floatX)
			b_layer2 = theano.shared(value = b_value_layer2, borrow = True)
			
		else:
			
			W_layer0 = theano.shared(value = init_params[0], borrow = True)
			b_layer0 = theano.shared(value = init_params[1], borrow = True)
			W_layer1 = theano.shared(value = init_params[2], borrow = True)
			b_layer1 = theano.shared(value = init_params[3], borrow = True)
			W_layer2 = theano.shared(value = init_params[4], borrow = True)
			b_layer2 = theano.shared(value = init_params[5], borrow = True)

		self.params = [W_layer0, b_layer0] + [W_layer1, b_layer1] +[W_layer2,b_layer2]	
		
		conv_out = conv.conv2d(
				input = self.input_board.dimshuffle('x','x',0,1),
				filters = W_layer0,
				filter_shape = filter_shape,
				image_shape = image_shape
				)
		layer0_output = T.tanh(conv_out + b_layer0.dimshuffle('x', 0, 'x', 'x'))

		layer1_input = layer0_output.flatten()

		layer1_output = T.tanh(T.dot(layer1_input, W_layer1) + b_layer1)
		layer2_input = layer1_output
		
		self.output = T.tanh(T.dot(layer2_input, W_layer2) + b_layer2)
		



	def get_q_value(self, input_board_value):

		f = theano.function(
			[self.input_board],
			self.output[0],
		)
		return f(input_board_value)



	def assign_reward(self, reward_value, input_board_value):

		reward = T.lscalar()
		cost = T.sqr(reward - self.output[0])
		grads = T.grad(cost, self.params)
		updates = [
				(param_i, param_i - LEARNING_RATE * grad_i) 
				for param_i, grad_i in zip(self.params, grads)
				]
		gradF = theano.function(
					[self.input_board]
					cost,
					updates = updates,
					givens={
						reward:reward_value
					}
				)
		return gradF(input_board_value)


	def get_all_params(self):

		f = theano.function(
				[self.input_board],
				self.params,
				on_unused_input='ignore' 
			)
		return f(numpy.zeros((10,10)))











def test_deep_learner():
	learner = DeepLearner()
	print learner.get_q_value(numpy.zeros((10,10)))
	print learner.assign_reward(-1,numpy.zeros((10,10)))
	print learner.get_q_value(numpy.zeros((10,10)))
	print learner.get_all_params()


if __name__ == '__main__':
 	test_deep_learner() 
