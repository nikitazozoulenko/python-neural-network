    #ADADELTA
    p = 0.95
    for j in range(len(layers)):
        if(network.W[j] is not None):
            network.E_grad2[j] = p * network.E_grad2[j] + (1-p) * dJdW[j] * dJdW[j]
            RMS_grad = np.sqrt(network.E_grad2[j] + epsilon)
            RMS_x = np.sqrt(network.E_x2[j] + epsilon)
            delta_x = - RMS_x / RMS_grad * dJdW[j]
            network.E_x2[j] = p * network.E_x2[j] + (1-p) * delta_x * delta_x
            network.W[j] += delta_x

    #SGD
    learning_rate = 0.01
    for j in range(len(layers)):
        if(network.W[j] is not None):
            network.W[j] -= learning_rate * dJdW[j]


    #MOMENTUM
    learning_rate = 0.05
    mu = 0.95
    for j in range(len(layers)):
        if(network.W[j] is not None):
            network.v[j] = mu * network.v[j] - learning_rate * dJdW[j]
            network.W[j] += network.v[j]

def train_network(network, dJdW, learning_rate, mu):
    #MOMENTUM
    for j in range(len(layers)):
        if(network.W[j] is not None):
            v[j] = mu * v[j] - learning_rate * dJdW[j]
            network.W[j] += v[j]

def train_network(network, dJdW, learning_rate, mu):
    #ADADELTA
    p = 0.95
    for j in range(len(layers)):
        if(network.W[j] is not None):
            E_grad2[j] = p * E_grad2[j] + (1-p) * dJdW[j] * dJdW[j]
            RMS_grad = np.sqrt(E_grad2[j] + epsilon)
            RMS_x = np.sqrt(E_x2[j] + epsilon)
            delta_x = - RMS_x / RMS_grad * dJdW[j]
            E_x2[j] = p * E_x2[j] + (1-p) * delta_x * delta_x
            network.W[j] += delta_x
