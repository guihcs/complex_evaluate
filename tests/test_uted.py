import unittest

from complex_evaluate.uted import u_ted, u_sim


class UTEDTestCase(unittest.TestCase):
    def test_single_node(self):
        t1 = ('a', [])
        t2 = ('a', [])
        dist, _ = u_ted(t1, t2)
        self.assertEqual(dist, 0)

    def test_single_node_diff(self):
        t1 = ('a', [])
        t2 = ('b', [])
        dist, _ = u_ted(t1, t2)
        self.assertEqual(dist, 0.8)

    def test_simple_trees(self):
        t1 = ('a', [
            ('b', [])
        ])
        t2 = ('a', [
            ('b', [])
        ])
        dist, _ = u_ted(t1, t2)
        self.assertEqual(dist, 0)

    def test_simple_trees_diff(self):
        t1 = ('a', [
            ('b', [])
        ])
        t2 = ('a', [
            ('c', [])
        ])
        dist, _ = u_ted(t1, t2)
        self.assertEqual(dist, 0.8)

    def test_simple_trees_delete(self):
        t1 = ('a', [
            ('b', [])
        ])
        t2 = ('a', [
        ])
        dist, m = u_ted(t1, t2)
        self.assertEqual(dist, 1)
        self.assertTrue((3, 0) in m)

    def test_simple_trees_insert(self):
        t1 = ('a', [
        ])
        t2 = ('a', [
            ('b', [])
        ])
        dist, m = u_ted(t1, t2)
        self.assertEqual(dist, 1)
        self.assertTrue((0, 3) in m)

    def test_simple_trees_insert_same_level(self):
        t1 = ('a', [
            ('b', [])
        ])
        t2 = ('a', [
            ('b', []),
            ('c', [])
        ])
        dist, m = u_ted(t1, t2)
        self.assertEqual(dist, 1)
        self.assertTrue((0, 4) in m)

    def test_all_different(self):
        t1 = ('a', [
            ('b', [
                ('c', [])
            ])
        ])
        t2 = ('x', [
            ('y', [
                ('z', [])
            ]),
            ('w', [])
        ])
        dist, _ = u_ted(t1, t2)
        self.assertAlmostEqual(dist, 3.4)

    def test_order_sensitivity(self):
        t1 = ('a', [
            ('b', []),
            ('c', [])
        ])
        t2 = ('a', [
            ('c', []),
            ('b', [])
        ])
        dist, _ = u_ted(t1, t2)
        self.assertEqual(dist, 0)

        t1 = ('a', [
            ('b', [
                ('c', [])
            ]),
            ('b', [
                ('d', [])
            ])
        ])
        t2 = ('a', [
            ('b', [
                ('d', [])
            ]),
            ('b', [
                ('c', [])
            ])
        ])
        dist, _ = u_ted(t1, t2)
        self.assertEqual(dist, 0)

    def test_sim_eq(self):
        t1 = ('a', [
            ('b', []),
            ('c', [])
        ])
        t2 = ('a', [
            ('b', []),
            ('c', [])
        ])
        s = u_sim(t1, t2)
        self.assertEqual(s, 1.0)

    def test_sim_neq(self):
        t1 = ('a', [
            ('b', []),
            ('c', [])
        ])
        t2 = ('1', [
            ('2', []),
            ('3', [])
        ])
        s = u_sim(t1, t2)
        self.assertAlmostEqual(s, 0.2)

    def test_sim_half(self):
        t1 = ('a', [
            ('b', []),
            ('c', []),
            ('d', [])
        ])
        t2 = ('a', [
            ('b', []),
        ])
        s = u_sim(t1, t2)
        self.assertEqual(s, 0.5)

if __name__ == '__main__':
    unittest.main()
