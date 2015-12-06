import numpy
import theano
import theano.tensor as T

class DeepLearner:

	def __init__(self, init_params = None):

		self.input_board = T.dmatrix('input_board')
		
		rng = numpy.random.RandomState(23455)
		n_in_layer0 = 9
		n_out_layer0 = 18
		W_bound_layer0 = numpy.sqrt(6. / (n_in_layer0 + n_out_layer0))	
		if init_params is None:
			W_layer0 = theano.shared(
					numpy.asarray(
						rng.uniform(
							low = -W_bound_layer0, 
							high = W_bound_layer0, 
							size = (n_in_layer0, n_out_layer0)),
						dtype = theano.config.floatX),
					borrow = True)
			b_value_layer0 = numpy.zeros((n_out_layer0,), dtype = theano.config.floatX)
			b_layer0 = theano.shared(value = b_value_layer0, borrow = True)

	
			n_in_layer1 = n_out_layer0
			n_out_layer1 = 1
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
			
		else:
			
			W_layer0 = theano.shared(value = init_params[0], borrow = True)
			b_layer0 = theano.shared(value = init_params[1], borrow = True)
			W_layer1 = theano.shared(value = init_params[2], borrow = True)
			b_layer1 = theano.shared(value = init_params[3], borrow = True)
			

		self.params = [W_layer0, b_layer0] + [W_layer1, b_layer1]
		
		
		layer0_output = T.tanh(T.dot(self.input_board.flatten(), W_layer0) + b_layer0)
 
		layer1_input = layer0_output
		
		self.output = T.tanh(T.dot(layer1_input, W_layer1) + b_layer1)
		



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
				(param_i, param_i - 0.07 * grad_i) 
				for param_i, grad_i in zip(self.params, grads)
				]
		gradF = theano.function(
					[self.input_board],
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