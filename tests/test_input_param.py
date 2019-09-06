import netomaton as ntm
import numpy as np


class TestInputParam:

    # test the input parameter using a Finite State Machine
    def test_fsm(self):

        states = {'locked': 0, 'unlocked': 1}
        transitions = {'PUSH': 'p', 'COIN': 'c'}

        adjacencies = [[1]]

        initial_conditions = [states['locked']]

        events = "cpcpp"

        def fsm_rule(n, c, event):
            if event == transitions['PUSH']:
                return states['locked']
            else:
                # COIN event
                return states['unlocked']

        activities, _ = ntm.evolve(initial_conditions, adjacencies, input=events, activity_rule=fsm_rule)

        np.testing.assert_equal([[0], [1], [0], [1], [0], [0]], activities)
