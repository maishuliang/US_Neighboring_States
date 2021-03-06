neighboring_states = {'AK': ['WA'],
 'AL': ['FL', 'GA', 'MS', 'TN'],
 'AR': ['LA', 'MO', 'MS', 'OK', 'TN', 'TX'],
 'AZ': ['CA', 'CO', 'NM', 'NV', 'UT'],
 'CA': ['AZ', 'HI', 'NV', 'OR'],
 'CO': ['AZ', 'KS', 'NE', 'NM', 'OK', 'UT', 'WY'],
 'CT': ['MA', 'NY', 'RI'],
 'DC': ['MD', 'VA'],
 'DE': ['MD', 'NJ', 'PA'],
 'FL': ['AL', 'GA'],
 'GA': ['AL', 'FL', 'NC', 'SC', 'TN'],
 'IA': ['IL', 'MN', 'MO', 'NE', 'SD', 'WI'],
 'ID': ['MT', 'NV', 'OR', 'UT', 'WA', 'WY'],
 'IL': ['IA', 'IN', 'KY', 'MO', 'WI'],
 'IN': ['IL', 'KY', 'MI', 'OH'],
 'KS': ['CO', 'MO', 'NE', 'OK'],
 'KY': ['IL', 'IN', 'MO', 'OH', 'TN', 'VA', 'WV'],
 'LA': ['AR', 'MS', 'TX'],
 'MA': ['CT', 'NH', 'NY', 'RI', 'VT'],
 'MD': ['DC', 'DE', 'PA', 'VA', 'WV'],
 'ME': ['NH'],
 'MI': ['IN', 'OH', 'WI'],
 'MN': ['IA', 'ND', 'SD', 'WI'],
 'MO': ['AR', 'IA', 'IL', 'KS', 'KY', 'NE', 'OK', 'TN'],
 'MS': ['AL', 'AR', 'LA', 'TN'],
 'MT': ['ID', 'ND', 'SD', 'WY'],
 'NC': ['GA', 'SC', 'TN', 'VA'],
 'ND': ['MN', 'MT', 'SD'],
 'NE': ['CO', 'IA', 'KS', 'MO', 'SD', 'WY'],
 'NH': ['MA', 'ME', 'VT'],
 'NJ': ['DE', 'NY', 'PA'],
 'NM': ['AZ', 'CO', 'OK', 'TX', 'UT'],
 'NV': ['AZ', 'CA', 'ID', 'OR', 'UT'],
 'NY': ['CT', 'MA', 'NJ', 'PA', 'VT'],
 'OH': ['IN', 'KY', 'MI', 'PA', 'WV'],
 'OK': ['AR', 'CO', 'KS', 'MO', 'NM', 'TX'],
 'OR': ['CA', 'ID', 'NV', 'WA'],
 'PA': ['DE', 'MD', 'NJ', 'NY', 'OH', 'WV'],
 'SD': ['IA', 'MN', 'MT', 'ND', 'NE', 'WY'],
 'TN': ['AL', 'AR', 'GA', 'KY', 'MO', 'MS', 'NC', 'VA'],
 'UT': ['AZ', 'CO', 'ID', 'NM', 'NV', 'WY'],
 'VA': ['DC', 'KY', 'MD', 'NC', 'TN', 'WV'],
 'WA': ['AK', 'ID', 'OR'],
 'TX': ['AR', 'LA', 'NM', 'OK'],
 'HI': ['CA'],
 'WY': ['CO', 'ID', 'MT', 'NE', 'SD', 'UT'],
 'RI': ['CT', 'MA'],
 'SC': ['GA', 'NC'],
 'WI': ['IA', 'IL', 'MI', 'MN'],
 'WV': ['KY', 'MD', 'OH', 'PA', 'VA'],
 'VT': ['MA', 'NH', 'NY'],
 'PR':['PR'],
 'AP':['AE'],
 'AE':['AP']}


# find the list of all neighboring states of a state
def find_neighboring_sates(state):

    if state in neighboring_states:
        return neighboring_states[state]
    else:
        raise Exception('State Not Found')
        
# check if 2 states are neighbors
def if_neighboring_states(state1, state2):

    if state1 not in neighboring_states:
        raise Exception('{} State Not Found'.format(state1))
    elif state2 not in neighboring_states:
        raise Exception('{} State Not Found'.format(state2))
    else:
        return state2 in neighboring_states[state1]
