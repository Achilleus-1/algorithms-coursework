#   CS-3343-004 Project 3

#section for taking in dictionary. then loads it into O(1) looker-upper
def load_dictionary(filename): 
    word_set = set()
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            if word:
                word_set.add(word)
    return word_set


# Just reads all input words from file and puts into python list
def read_input(filename):
    inputs = []
    with open(filename, 'r') as f:
        for line in f:
            inputs.append(line.strip())
    return inputs



#fits what was said in lectures to be "dynamic". finds min num of dictionary words to split from input
def split_string(s, word_set):

    n = len(s)
    dp = [float('inf')] * (n + 1)
    next_index = [-1] * (n + 1)
    dp[n] = 0  # base case: empty suffix needs 0 words

#tries all longish words first and update dp[i] if a better/shorter split is found
    for i in range(n - 1, -1, -1):
        for j in range(n, i, -1):  

# basically is added so that theres no issues with longerwords, especially "wholesome thing" like in the expected output. fixes that.
            if s[i:j] in word_set and dp[j] != float('inf'):

                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
                    next_index[i] = j

# if index start cant be split into valid words, returns None
    if dp[0] == float('inf'):

        return None


#array to rebuild words as split
    words = []
    idx = 0
    while idx < n:
        next_idx = next_index[idx]
        words.append(s[idx:next_idx])
        idx = next_idx

    return words


#loads dictionary and list of inputs. I changed it from the example readDictionary to more easily work "dynamically"
#Instead of manually checking just the set words, Im loading the dictionary into a set and returning tge set to split input strings properly and dynamically. guidelines dont say i have to exactly copy it if thats ok.
def main():
    dictionary = load_dictionary('aliceInWonderlandDictionary.txt')
    inputs = read_input('input.txt')



# fir each input, find optimal split, print it like the output example says
    for s in inputs:
        result = split_string(s, dictionary)
        if result is None:
            print("{} cannot be split into AiW words.".format(s)) #fixed formatting for fox servers
        else:
            num_words = len(result)
            split_words = ' '.join(result)
            print("{} can be split into {} AiW word{}: {}".format(s, num_words, 's' if num_words != 1 else '', split_words)) #fixed formatting for fox servers



# runs function when script is started
if __name__ == "__main__":
    main()
