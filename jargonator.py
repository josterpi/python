#!/usr/bin/env python

#Column 1                Column 2                Column 3

#0. integrated           0. management           0. options
#1. total                1. organizational       1. flexibility
#2. systematized         2. monitored            2. capability
#3. parallel             3. reciprocal           3. mobility
#4. functional           4. digital              4. programming
#5. responsive           5. logistical           5. concept
#6. optional             6. transitional         6. time-phase
#7. synchronized         7. incremental          7. projection
#8. compatible           8. third-generation     8. hardware
#9. balanced             9. policy               9. contingency

# The procedure is simple.  Think of any three-digit number, then select
#the corresponding buzzword from each column.  For instance, number 257 produces
#"systematized logistical projection," a phrase that can be dropped into
#virtually any report with that ring of decisive, knowledgeable authority.  "No
#one will have the remotest idea of what you're talking about," says Broughton,
#"but the important thing is that they're not about to admit it."
#            -- Philip Broughton, "How to Win at Wordsmanship"
			

import random
first = ['integrated','total','systematized','parallel','functional','responsive','optional','synchronized','compatible','balanced']
second = ['management','organizational','monitored','reciprocal','digital','logistical','transitional','incremental','third-generation','policy']
third = ['options','flexibility','capability','mobility','programming','concept','time-phase','projection','hardware','contingency']
#print first[random.randrange(9)] . ' ' . second[random.randrange(9)] . ' ' . third[random.randrange(9)]
print random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(third)
