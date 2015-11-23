# lst
length-constrained maximum-sum subtree algorithms


# Processing of messages

- removed "\ "
- removed "= "
- removed "[IMAGE]"


Def of word:

1. only alphabetic letters: 14981 unique tokens
2. otherwise:  21862 unique tokens


# Topics

1. davis utilities san plant plants times million utility blackouts generators commission customers trading companies percent electric officials federal wed edison [California eletricity crisis](https://en.wikipedia.org/wiki/California_electricity_crisis)
2. ect iso enronxgate amto confidential report draft enroncc susan joe communications ken comments order david june transmission markets language chairman [Ken's email](https://www.cs.umd.edu/~golbeck/perl/examples/KenLayEmail.txt)
3. bush jones president dow stock bank companies trading dynegy confidential news service natural oil credit services copyright deal percent policies [Bush and Ken Lay: Slip Slidin' Away](https://consortiumnews.com/Print/020602.html)
4. davis utilities edison billion federal generators utility commission governor plan million crisis san plants electric pay companies thursday iso southern. [Davis buy transmission lines](http://www.consumerwatchdog.org/story/davis-reaches-deal-edison-buy-transmission-lines-27-billion)


# Resources

- [Enron Criss Timeline][https://www.ferc.gov/industries/electric/indus-act/wec/chron/chronology.pdf]


# Dairy

Day 1: 

- improved preprocessing
- checked the topic results
- meta graph construction(decomposing multiple-recipients node, add weight to edge, round to fixed decimal point)

Day 2:

- binarize general DAG, add reward attribute to node(as we need to create dummy nodes)
- preprocess enron.json
- Write the algorithm that gets A_u[i] for all nodes
- Q: what do events with highest score look like? what are the top K events?
- parameter tuning(embedded task)
