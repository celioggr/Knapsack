# Knapsack
> A simple (yet functional) PKC algorithm based on Knapsack

This work is my first approach into the PKC world. This implementation intends to be a light-weight public-key cryptosystem based on the [subset sum problem](https://en.wikipedia.org/wiki/Subset_sum_problem) (a special case of the knapsack problem) which is known to be **NP-Complete**.

### KeyGen

* Choose a superincreasing sequence with enough elements (notice that implementations of this algorithm are no longer considered secure nowadays. So you must choose a Knapsack at least with 250 elements and these must be within the range of 200 to 400bits to be used in practice).
The following superincreasing sequence will be our private key.


![Knapsack1](https://i.imgur.com/mzE9kzK.png)


* Pick random integers m, n such that:


![Knapsack2](https://i.imgur.com/aQqbIoI.png)

* Calculate public key by computing the following to every element on the knapsack.



 **βi = n*xi mod p** 
 


 > Kp = {β1, β2, ... , βi} - computed values above will be the public key






### Cipher


To cipher a message with k bits, just compute the following and represent the correspondent integers.

![Knapsack3](https://i.imgur.com/zClQcbq.png)

An example. For the message **011010110101** the process will look like this.

![Knapsack4](https://i.imgur.com/ZMZ5Rnx.png)

> Our ciphered message is {276,280}



### Decipher


In order to decipher a ciphertext c a receiver has to find the message bits αi such that they satisfy:

![Knapsack5](https://i.imgur.com/VzZ4BVz.png)

This would be a hard problem if the βi were random values because the receiver would have to solve an instance of the subset sum problem, which is known to be **NP-hard**. However, the values βi were chosen such that decryption is easy if the private key is known.
Given that, we only need to find an integer **s** that is the **modular inverse of n mod m** (*Extended Euclidean algorithm*).


Then the receiver of the ciphertext c computes:



![Knapsack6](https://i.imgur.com/hKN2u8P.png)


Taking the same example presented before, the process will look like this where the modular inverse of n is 61.


![Knapsack7](https://i.imgur.com/PUYSlWj.png)


Now the receiver only has to solve the subset sum problem (which is easy because the knapsack is a superincreasing sequence).

![Knapsack8](https://i.imgur.com/l6OShie.png)


Finally, the last step of our example will look like this. Notice that original message was recovered.


![Knapsack9](https://i.imgur.com/TTsnIFh.png)













