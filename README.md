User inputs the number of participants who take part in the secret santa, and then all names. 
All participants, identified by their names are saved in a list (part_from). 
Then we create a part_to list which contains the names of the participants in a different order, so that with both lists we have a matching person A gives a present to person B, etc.
We want to ensure that no one has to buy a present for themselves, so we prevent, for any i index, that part_from[i]=part_to[i]. 
In the end, all matched "couples" are saved in a dictionary where the present givers are the keys, and the present receivers are the values. 
