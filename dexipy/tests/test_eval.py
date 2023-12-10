import unittest
from copy import deepcopy
from dexipy.eval import evaluation_order, eval_parameters, EvalMethods
from dexipy.eval import evaluate_as_set, evaluate_as_distribution, evaluate
from dexipy.dexi import read_dexi_from_string
from dexipy.tests.testdata import car_xml, car2_xml, linked_xml, continuous_old_xml, continuous_new_xml, continuous_new_no_alt_xml, dozen_xml

def unchanged_alternative(alt1, alt2, ids = []) -> bool:
    if not (isinstance(alt1, dict) and isinstance(alt2, dict)):
        return False
    for id in ids:
        if alt1[id] != alt2[id]:
            return False
    return True

def unchanged(alts1, alts2, ids = []) -> bool:
    if len(alts1) != len(alts2):
        return False
    for idx, alt in enumerate(alts1):
        alt1 = alts1[idx]
        alt2 = alts2[idx]
        if not unchanged_alternative(alt1, alt2, ids):
            return False
    return True

class Test_test_eval(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.car_dxi = read_dexi_from_string(car_xml)
        cls.car2_dxi = read_dexi_from_string(car2_xml)
        cls.linked_dxi = read_dexi_from_string(linked_xml)
        cls.continuous_old_dxi = read_dexi_from_string(continuous_old_xml)
        cls.continuous_new_dxi = read_dexi_from_string(continuous_new_xml)
        cls.continuous_new_no_alt_dxi = read_dexi_from_string(continuous_new_no_alt_xml)
        cls.dozen_dxi = read_dexi_from_string(dozen_xml)
        return super().setUpClass()

    def test_evaluation_order_Car(self):
        ord = evaluation_order(self.car_dxi.root)
        self.assertEqual(ord, ["BUY.PRICE", "MAINT.PRICE", "PRICE", "#PERS", "#DOORS", "LUGGAGE", "COMFORT", "SAFETY", "TECH.CHAR.", "CAR", "CAR_MODEL"])
        ord = evaluation_order(self.car_dxi.attrib("PRICE"))
        self.assertEqual(ord, ["BUY.PRICE", "MAINT.PRICE", "PRICE"])
        ord = evaluation_order(self.car_dxi.root, prune = ["COMFORT"])
        self.assertEqual(ord, ["BUY.PRICE", "MAINT.PRICE", "PRICE", "COMFORT", "SAFETY", "TECH.CHAR.", "CAR", "CAR_MODEL"])
        ord = evaluation_order(self.car_dxi.root, prune = ["TECH.CHAR.", "PRICE"])
        self.assertEqual(ord, ["PRICE", "TECH.CHAR.", "CAR", "CAR_MODEL"])

    def test_evaluation_order_Linked(self):
        ord = evaluation_order(self.linked_dxi.root)
        self.assertEqual(ord, ['A_2', 'A', 'B_2', 'B', 'MIN', 'A_1', 'B_1', 'MAX', 'MID', 'LinkedBoundsTest', 'root'])
        ord = evaluation_order(self.linked_dxi.root, prune = ["MAX"])
        self.assertEqual(ord, ['A_2', 'A', 'B_2', 'B', 'MIN', 'MAX', 'MID', 'LinkedBoundsTest', 'root'])

    def test_EvalMethods_Linked(self):
        self.assertEqual(len(EvalMethods._eval_methods.keys()), 4)
        self.assertEqual(list(EvalMethods._eval_methods.keys()), ["set", "prob", "fuzzy", "fuzzynorm"])

    def test_evaluate_as_set_Car_CAR(self):
        att = self.car_dxi.attrib("CAR")
        fnc = att.funct

        inps = [0, 0]
        eval = evaluate_as_set(fnc, inps)
        self.assertEqual(eval, {0})

        inps = [1, 1]
        eval = evaluate_as_set(fnc, inps)
        self.assertEqual(eval, {1})

        inps = [{1,0}, 1]
        eval = evaluate_as_set(fnc, inps)
        self.assertEqual(eval, {0, 1})

        inps = [{1,0}, {1,2}]
        eval = evaluate_as_set(fnc, inps)
        self.assertEqual(eval, {0, 1, 2})

    def test_evaluate_as_set_Car_SetExpandedCAR(self):
        att = self.car_dxi.attrib("CAR")
        fnc = deepcopy(att.funct)
        fnc.values[(0,0)] = {0, 1}

        inps = [0, 0]
        eval = evaluate_as_set(fnc, inps)
        self.assertEqual(eval, {0, 1})

        inps = [1, 1]
        eval = evaluate_as_set(fnc, inps)
        self.assertEqual(eval, {1})

        inps = [{2,0}, {3,0}]
        eval = evaluate_as_set(fnc, inps)
        self.assertEqual(eval, {0, 1, 3})

    def test_evaluate_as_distribution_prob_Car_CAR(self):
        att = self.car_dxi.attrib("CAR")
        fnc = att.funct
        eval_param = eval_parameters("prob")

        inps = [[1], 0]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [1, 0, 0, 0])

        inps = [[1, 0, 1], 0]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [2, 0, 0, 0])

        inps = [[0.1, 0.3, 0.6], [0.1, 0.2, 0.3, 0.4]]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [0.19, 0.06, 0.21, 0.54])

    def test_evaluate_as_distribution_fuzzy_Car_CAR(self):
        att = self.car_dxi.attrib("CAR")
        fnc = att.funct
        eval_param = eval_parameters("fuzzy")

        inps = [[1], 0]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [1, 0, 0, 0])

        inps = [[1, 0, 1], 0]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [1, 0, 0, 0])

        inps = [[0.1, 0.3, 0.6], [0.1, 0.2, 0.3, 0.4]]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [0.1, 0.2, 0.3, 0.4])

        inps = [[0.2, 0.4, 1], [0.1, 0.5, 0.7, 1]]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [0.2, 0.4, 0.5, 1])

    def test_evaluate_as_distribution_prob_Car_SetExpandedCAR(self):
        att = self.car_dxi.attrib("CAR")
        fnc = deepcopy(att.funct)
        fnc.values[(0,0)] = {0, 1}
        fnc.values[(1,0)] = {1, 2}
        eval_param = eval_parameters("prob")

        inps = [[1], 0]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [0.5, 0.5, 0, 0])

        inps = [[1, 0, 1], 0]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        self.assertEqual(eval, [1.5, 0.5, 0, 0])

        inps = [[0.1, 0.3, 0.6], [0.1, 0.2, 0.3, 0.4]]
        eval = evaluate_as_distribution(fnc, inps, eval_param)
        expect = [0.155, 0.08, 0.225, 0.54]
        self.assertEqual(len(eval), len(expect))
        self.assertEqual(sum(eval), 1.0)
        for idx, el in enumerate(eval):
            self.assertAlmostEqual(el, expect[idx])

    def test_PlainEvaluation_Car(self):
        alts0 = self.car_dxi.alternatives
        alts = deepcopy(alts0)
        for id in self.car_dxi.aggregate_ids:
            for alt in alts:
                alt[id] = None
        eval = evaluate(self.car_dxi, alts)
        self.assertTrue(unchanged(alts0, eval, self.car_dxi.non_root_ids))

    def test_PlainPrunedEvaluation_Car(self):
        alts0 = self.car_dxi.alternatives
        alts = deepcopy(alts0)
        for id in self.car_dxi.aggregate_ids:
            if id != "PRICE":
                for alt in alts:
                    alt[id] = None
        eval = evaluate(self.car_dxi, alts, prune = ["PRICE"])
        check = ['CAR', 'PRICE', 'TECH.CHAR.', 'COMFORT', '#PERS', '#DOORS', 'LUGGAGE', 'SAFETY']
        self.assertTrue(unchanged(alts0, eval, check))
        for id in ['BUY.PRICE','MAINT.PRICE']:
            for alt in eval:
                self.assertEqual(alt[id], None)

    def test_SetEvaluation_Car(self):
        alt0 = self.car_dxi.alternatives[0]
        alt = self.car_dxi.alternative(alt = alt0, values = {"BUY.PRICE": "*"})
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt)
        check = ['MAINT.PRICE', 'TECH.CHAR.', 'COMFORT', '#PERS', '#DOORS', 'LUGGAGE', 'SAFETY']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["BUY.PRICE"], {0, 1, 2})
        self.assertEqual(eval["PRICE"], {0, 2})
        self.assertEqual(eval["CAR"], {0, 3})

        alt0 = self.car_dxi.alternatives[1]
        alt = self.car_dxi.alternative(alt = alt0, SAFETY = "*")
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt)
        check = ['PRICE', 'BUY.PRICE', 'MAINT.PRICE', 'COMFORT', '#PERS', '#DOORS', 'LUGGAGE']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["TECH.CHAR."], {0, 2, 3})
        self.assertEqual(eval["CAR"], {0, 2, 3})

        alt0 = self.car_dxi.alternatives[1]
        alt = self.car_dxi.alternative(alt = alt0, SAFETY = {1, 2})
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt)
        check = ["PRICE", "BUY.PRICE", "MAINT.PRICE", "COMFORT", "#PERS", "#DOORS", "LUGGAGE"]
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["SAFETY"], {1, 2})
        self.assertEqual(eval["TECH.CHAR."], {2, 3})
        self.assertEqual(eval["CAR"], {2, 3})

    def test_ProbEvaluation_Car(self):
        alt0 = self.car_dxi.alternatives[0]
        alt = self.car_dxi.alternative(alt = alt0, values = {"BUY.PRICE": "*"})
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt, method = "prob")
        check = ['MAINT.PRICE', '#PERS', '#DOORS', 'LUGGAGE', 'SAFETY']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["BUY.PRICE"], {0, 1, 2})
        self.assertEqual(eval["TECH.CHAR."], 3)
        self.assertEqual(eval["COMFORT"], 2)
        self.assertEqual(eval["PRICE"], [1/3, 0, 2/3])
        self.assertEqual(eval["CAR"], [1/3, 0, 0, 2/3])

        alt0 = self.car_dxi.alternatives[1]
        alt = self.car_dxi.alternative(alt = alt0, SAFETY = "*")
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt, method = "prob")
        check = ['BUY.PRICE', 'MAINT.PRICE', '#PERS', '#DOORS', 'LUGGAGE']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["SAFETY"], {0, 1, 2})
        self.assertEqual(eval["COMFORT"], 2)
        self.assertEqual(eval["TECH.CHAR."], [1/3, 0, 1/3, 1/3])
        self.assertEqual(eval["CAR"], [1/3, 0, 1/3, 1/3])

        alt0 = self.car_dxi.alternatives[1]
        alt = self.car_dxi.alternative(alt = alt0, SAFETY = {1, 2})
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt, method = "prob")
        check = ['BUY.PRICE', 'MAINT.PRICE', '#PERS', '#DOORS', 'LUGGAGE']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["SAFETY"], {1, 2})
        self.assertEqual(eval["COMFORT"], 2)
        self.assertEqual(eval["TECH.CHAR."], [0, 0, 1/2, 1/2])
        self.assertEqual(eval["CAR"], [0, 0, 1/2, 1/2])

    def test_FuzzyEvaluation_Car(self):
        alt0 = self.car_dxi.alternatives[0]
        alt = self.car_dxi.alternative(alt = alt0, values = {"BUY.PRICE": "*"})
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt, method = "fuzzy")
        check = ['MAINT.PRICE', '#PERS', '#DOORS', 'LUGGAGE', 'SAFETY']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["BUY.PRICE"], {0, 1, 2})
        self.assertEqual(eval["TECH.CHAR."], 3)
        self.assertEqual(eval["COMFORT"], 2)
        self.assertEqual(eval["PRICE"], {0, 2})
        self.assertEqual(eval["CAR"], {0, 3})

        alt0 = self.car_dxi.alternatives[1]
        alt = self.car_dxi.alternative(alt = alt0, SAFETY = "*")
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt, method = "fuzzy")
        check = ['BUY.PRICE', 'MAINT.PRICE', '#PERS', '#DOORS', 'LUGGAGE']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["SAFETY"], {0, 1, 2})
        self.assertEqual(eval["COMFORT"], 2)
        self.assertEqual(eval["TECH.CHAR."], {0, 2, 3})
        self.assertEqual(eval["CAR"], {0, 2, 3})

        alt0 = self.car_dxi.alternatives[1]
        alt = self.car_dxi.alternative(alt = alt0, SAFETY = {1, 2})
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt, method = "fuzzy")
        check = ['BUY.PRICE', 'MAINT.PRICE', '#PERS', '#DOORS', 'LUGGAGE']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["SAFETY"], {1, 2})
        self.assertEqual(eval["COMFORT"], 2)
        self.assertEqual(eval["TECH.CHAR."], {2, 3})
        self.assertEqual(eval["CAR"], {2, 3})

        alt0 = self.car_dxi.alternatives[1]
        alt = self.car_dxi.alternative(alt = alt0, SAFETY = [0, 0.2, 0.5])
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt, method = "fuzzy")
        check = ['BUY.PRICE', 'MAINT.PRICE', '#PERS', '#DOORS', 'LUGGAGE']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["SAFETY"], [0, 0.2, 0.5])
        self.assertEqual(eval["COMFORT"], 2)
        self.assertEqual(eval["TECH.CHAR."], [0, 0, 0.2, 0.5])
        self.assertEqual(eval["CAR"], [0, 0, 0.2, 0.5])


    def test_FuzzyNormEvaluation_Car(self):
        alt0 = self.car_dxi.alternatives[1]
        alt = self.car_dxi.alternative(alt = alt0, SAFETY = [0, 0.2, 0.5])
        for id in self.car_dxi.aggregate_ids:
            alt[id] = None
        eval = evaluate(self.car_dxi, alt, method = "fuzzynorm")
        check = ['BUY.PRICE', 'MAINT.PRICE', '#PERS', '#DOORS', 'LUGGAGE']
        self.assertTrue(unchanged_alternative(alt0, eval, check))
        self.assertEqual(eval["SAFETY"], [0, 0.4, 1])
        self.assertEqual(eval["COMFORT"], 2)
        self.assertEqual(eval["TECH.CHAR."], [0, 0, 0.4, 1])
        self.assertEqual(eval["CAR"], [0, 0, 0.4, 1])

    def test_PlainEvaluation_Linked(self):
        model = self.linked_dxi
        alts0 = model.alternatives
        alts = deepcopy(alts0)
        for id in model.aggregate_ids:
            for alt in alts:
                alt[id] = None
        eval = evaluate(model, alts)
        self.assertTrue(unchanged(alts0, eval, model.non_root_ids))

    def test_PlainEvaluation_ContinuousNew(self):
        model = self.continuous_new_dxi
        alts0 = model.alternatives
        alts = deepcopy(alts0)
        for id in model.aggregate_ids:
            for alt in alts:
                alt[id] = None
        eval = evaluate(model, alts)
        self.assertEqual(eval[0], {'name': 'Null/Null', 'OneLevel': None, 'X1': None, 'N1': None, 'X2': None, 'N2': None})
        self.assertEqual(eval[1], {'name': 'Null/All', 'OneLevel': None, 'X1': None, 'N1': None, 'X2': None, 'N2': None})
        self.assertEqual(eval[2], {'name': 'Test1', 'OneLevel': 0, 'X1': 0, 'N1': -2.0, 'X2': 0, 'N2': -2.0})
        self.assertEqual(eval[3], {'name': 'Test2', 'OneLevel': {0, 1}, 'X1': 0, 'N1': -2.0, 'X2': 1, 'N2': 0.0})
        self.assertEqual(eval[4], {'name': 'Test3', 'OneLevel': 2, 'X1': 0, 'N1': -2.0, 'X2': 2, 'N2': 2.0})
        self.assertEqual(eval[5], {'name': 'Test4', 'OneLevel': {1, 2}, 'X1': 1, 'N1': 2.0, 'X2': 0, 'N2': -2.0})
        self.assertEqual(eval[6], {'name': 'Test5', 'OneLevel': 2, 'X1': 1, 'N1': 2.0, 'X2': 1, 'N2': 0.0})
        self.assertEqual(eval[7], {'name': 'Test6', 'OneLevel': 2, 'X1': 1, 'N1': 2.0, 'X2': 2, 'N2': 2.0})
        self.assertEqual(eval[8], {'name': 'Test7', 'OneLevel': {0, 1}, 'X1': 0, 'N1': 0.0, 'X2': 1, 'N2': 0.0})

    def test_PlainEvaluation_Dozen(self):
        model = self.linked_dxi
        alts0 = model.alternatives
        alts = deepcopy(alts0)
        for id in model.aggregate_ids:
            for alt in alts:
                alt[id] = None
        eval = evaluate(model, alts)
        self.assertTrue(unchanged(alts0, eval, model.non_root_ids))

if __name__ == '__main__':
    unittest.main()
