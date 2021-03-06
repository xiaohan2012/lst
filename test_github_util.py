import os
import unittest
from .util import json_load
from .github_util import (make_dataframe,
                          dump2interactions,
                          dump2people,
                          remove_messages_post_by_certain_users)
from .test_util import make_path
from .thread_util import KEY_THREAD_ID

from nose.tools import assert_equal, assert_true


class GithubUtilTest(unittest.TestCase):
    def setUp(self):
        self.df = make_dataframe(
            make_path('test/data/sklearn/raw.json')
        )

    def test_make_dataframe(self):
        assert_equal(6, self.df.shape[1])
        assert_equal(1, self.df.iloc[0][KEY_THREAD_ID])
        assert_equal(1, self.df.iloc[1][KEY_THREAD_ID])
        assert_equal(
            "Document multilabel y support for all splitters in model_selection module",
            self.df.iloc[0]['subject']
        )
        assert_equal(
            "RE: Document multilabel y support for all splitters in model_selection module",
            self.df.iloc[1]['subject']
        )
        assert_true(' '.join(["L(Documentation)", "L(Easy)",
                              "L(Need Contributor)"])
                    in self.df.iloc[0]['body'])
        assert_equal(
            len(json_load(make_path('test/data/sklearn/raw.json'))) - 1,
            self.df.iloc[-1][KEY_THREAD_ID]
        )

    def test_dump2interactions(self):
        output_path = make_path('test/data/tmp/blah.json')
        dump2interactions(make_path('test/data/sklearn/raw.json'),
                          output_path)

        interactions = json_load(output_path)
        assert_equal(9358, len(interactions))
        for i in interactions:
            assert_true('recipient_ids' in i)

        os.remove(output_path)

    def test_dump2people(self):
        output_path = make_path('test/data/tmp/people.json')
        dump2people(make_path('test/data/sklearn/raw.json'),
                    output_path)
        people = json_load(output_path)
        assert_equal({'id': 'MechCoder'}, people[0])
        assert_equal(669, len(people))

    def test_remove_messages_post_by_certain_users(self):
        assert_true(
            self.df[self.df['sender_id'] == 'coveralls'].shape[0] > 0
        )
        df = remove_messages_post_by_certain_users(
            self.df, ['coveralls']
        )
        assert_equal(
            0,
            df[df['sender_id'] == 'coveralls'].shape[0]
        )
        
