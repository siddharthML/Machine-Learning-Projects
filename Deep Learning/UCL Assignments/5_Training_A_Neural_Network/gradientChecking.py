import numpy as np

def checkNNGradients(small_nnet,X):
#CHECKNNGRADIENTS checks the backpropagation gradients for a small neural network
#   it will output the analytical gradients
#   produced by your backprop code and the numerical gradients (computed
#   using compute_numerical_gradient). These two gradient computations should
#   result in very similar values.
    m = len(X)
    grad_b = [np.zeros(b.shape) for b in small_nnet.biases]
    grad_w = [np.zeros(w.shape) for w in small_nnet.weights]
    num_grad_b=grad_b
    num_grad_w=grad_w
    
    for x, y in X:
        delta_grad_b, delta_grad_w = small_nnet.backprop(x, y) # take an example backpropagate to find the gradients
        grad_b = [nb+dnb for nb, dnb in zip(grad_b, delta_grad_b)] # accumulate gradients for biases
        grad_w = [nw+dnw for nw, dnw in zip(grad_w, delta_grad_w)] # accumulate gradients for weights
        
    for x, y in X:        
        delta_grad_b, delta_grad_w = compute_numerical_gradient(small_nnet,x,y) # lists indexed by layer
        num_grad_b = [nb+dnb for nb, dnb in zip(num_grad_b, delta_grad_b)] # accumulate gradients for biases
        num_grad_w = [nw+dnw for nw, dnw in zip(num_grad_w, delta_grad_w)] # accumulate gradients for weights
    l=0
    for n_g_w ,g_w in zip(num_grad_w,grad_w):
        
        #print('Numeri',n_g_w/m)
        #print('Analyt',g_w/m)
        dif = n_g_w - g_w 
        dif_flat = dif.flatten()
        numerator = np.linalg.norm(dif_flat)
        denominator = np.linalg.norm(n_g_w.flatten()) + np.linalg.norm(g_w.flatten())
        #print(numerator,denominator)
        criterion= numerator/denominator
        print('Relative difference',criterion, 'for layer',l,'parameters')
        l+=1
        if criterion > 1e-5:
            print('error with backprop')
            
        else:
            print('Analytical and numerical gradients match')
            print('as relative distance is less that 1e-5')
    
        
    
def compute_numerical_gradient(small_nnet,x,y):
    e = 1e-8
    X=[(x,y)] 
    # save actual weigths
    saved_weights = small_nnet.weights
    saved_biases = small_nnet.biases
    
    weights=saved_weights
    biases =saved_biases

    num_grad_b=[]
    num_grad_w=[]
    
    for k in range(len(weights)):
        num_grad_w.append(np.zeros(weights[k].shape))
        num_grad_b.append(np.zeros(biases[k].shape))

    l=0
    
    for ws,bs in zip(saved_weights,saved_biases):
        # reset the weights to their actual values
        #weights=saved_weights
        #biases =saved_biases
        perturbations= np.zeros(ws.shape)
        #print('l',l)
        for i in range(ws.shape[0]):
            for j in range(ws.shape[1]):
                
                perturbations[i,j]=e # add e to one param
                ws_perturbed_plus =ws + perturbations # perturb parameters
                weights[l]=ws_perturbed_plus # move perturbed weights to weights list  
                
                small_nnet.weights=weights   # set the networks weights equal to the perturbed weights
                loss1 = small_nnet.cost_function(X)
                #print('L1',loss1)

                ws_perturbed_minus = ws - perturbations
                weights[l]=ws_perturbed_minus
                
                small_nnet.weights=weights
                loss2 = small_nnet.cost_function(X)
                #print('L2',loss2)
                                
                num_grad_w[l][i,j]=(loss1-loss2)/(2*e)
                
                weights=saved_weights # reset weights to their original value
                perturbations[i,j]=0  # undo perturbation
        
        l+=1
        small_nnet.weights=saved_weights

    return num_grad_b,num_grad_w  



   

