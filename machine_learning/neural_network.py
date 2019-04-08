import numpy as np

def sigmoid(x):
	# Sigmoid activation function: f(x) = 1 / (1 + e^(-x))
	return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
	# Derivative of sigmoid: f'(x) = f(x)(1 - f(x))
	fx = sigmoid(x)
	return fx * (1 - fx)

def mes_loss(y_true, y_pred):
	# Mean square error
	return ((y_pred - y_true) ** 2).mean()

class NeuralNetwork:
	'''
	A neural network with:
    - 2 inputs
    - 1 hidden layer with 2 neurons (h1, h2)
    - 1 output layer with 1 neuron (o1) 
	'''
	def __init__(self):
		# weights
		self.w1 = np.random.normal()
		self.w2 = np.random.normal()
		self.w3 = np.random.normal()
		self.w4 = np.random.normal()
		self.w5 = np.random.normal()
		self.w6 = np.random.normal()

		# biases
		self.b1 = np.random.normal()
		self.b2 = np.random.normal()
		self.b3 = np.random.normal()

	def feedforward(self, x):
		# x is a numpy array with 2 elements
		h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
		h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
		o1 = sigmoid(self.w5 * x[0] + self.w6 * x[1] + self.b3)
		return o1

	def train(self, data, labels):
		'''
		- data is a (n x 2) numpy array, n is the number of samples in dataset
		- labels is a numpy array with n elements, which correspond to those in data
		'''
		learn_rate = 0.1
		epochs = 1000 # times to loop through the entire dataset

		for epoch in range(epochs):
			for x, y_true in zip(data, labels):
				# feedforward
				sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
				h1 = sigmoid(sum_h1)

				sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
				h2 = sigmoid(sum_h2)

				sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
				o1 = sigmoid(sum_o1)
				y_pred = o1

				# calculate the partial derivatives
				# d_L_d_w1 represents "partial L / partial w1"
				d_L_d_ypred = -2 * (y_true - y_pred)

				# neural o1
				d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
				d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)
				d_ypred_d_b3 = deriv_sigmoid(sum_o1)

				d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)
				d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)

				# neural h1
				d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
				d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
				d_h1_d_b1 = deriv_sigmoid(sum_h1)

				# neural h2
				d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
				d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
				d_h2_d_b2 = deriv_sigmoid(sum_h2)

				# Update weights and biases
				# neural h1
				self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
				self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
				self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

				# neural h2
				self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
				self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
				self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

				# neural o1
				self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
				self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
				self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

				if epoch % 10 == 0:
					y_preds = np.apply_along_axis(self.feedforward, axis=1, arr=data)
					loss = mes_loss(labels, y_preds)
					print('Epoch %d loss: %.3f' % (epoch, loss))

if __name__ == '__main__':
	data = np.array([[-2, -1], [25, 6], [17, 4], [-15, -6]])
	labels = np.array([1, 0, 0, 1])
	network = NeuralNetwork()
	network.train(data, labels)

	# Make some predictions
	tom = np.array([-7, -3])
	lee = np.array([20, 2])
	print('tom: %.3f' % network.feedforward(tom))
	print('lee: %.3f' % network.feedforward(lee))










