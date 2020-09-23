# This is an assignment on the problem of text mining. We are given a dataset of opinions of a group of people regarding the question “What qualities do you think are necessary to be a prime minister of India?” The task is to find the significant qualities from the opinions using Wordnet, an English lexical database and analyse the performance of our method by comparing our results with the human coding i.e., significant qualities found by some experts.
# Dataset: The dataset contains the opinions of 38 different people on the following question:
              “What qualities do you think are necessary to be a prime minister of India?”
# The opinions are mainly short texts which state the qualities of an ideal prime minister according to the respective people.

# Methodology
# The steps involved in finding the significant qualities from the given dataset are as follows:
# 	1. We form the temporary vocabulary of the dataset by considering only the nouns and adjectives from the text. We ignore the other words since the objective is to find the qualities of the prime minister. We then find the frequency of each term in the temporary vocabulary and arrange the terms in order of decreasing frequency.
# 	2. We find the synsets with respect to nouns and adjective only, for each word using Wordnet and store them in a list. We then find the derivationally related forms of each synset and then find the synsets of those forms and store them in another list. Finally, we add these two lists and form the main vocabulary containing the synsets of both the original terms and the derivationally related forms.
# 	3. Next, we find similar terms from the main vocabulary by using Wu-Palmer’s Similarity and merge those terms to form a cluster, for which the similarity score is greater than a given threshold value (= 0.9).
# 	4. We ignore the empty clusters and assign the remaining clusters to the original terms of the text if the term is present in the cluster. Here, we combine the terms which have the same clusters.
# 	5. Finally, we obtain the names corresponding to each synset present in the clusters of each term. We then recalculate the frequency of each cluster and arrange them in decreasing order of frequency.

# Alongwith Wu-Palmer's Similarity measure, we also worked on the dataset and found clusters using Path Similarity measure.
