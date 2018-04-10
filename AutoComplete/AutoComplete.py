
from collections import defaultdict
import codecs
import pickle


class AutoCompleter(object):



    filehandler = open('AutoComplete/token_to_exercise_name.obj', 'r')
    token_to_exercise_name = pickle.load(filehandler)

    filehandler = open('AutoComplete/n_gram_to_tokens.obj', 'r')
    n_gram_to_tokens = pickle.load(filehandler)

    def _get_real_tokens_from_possible_n_grams(self, tokens):
        real_tokens = []
        for token in tokens:
            token_set = self.n_gram_to_tokens.get(token, set())
            real_tokens.extend(list(token_set))
        return real_tokens

    def _get_scored_exercises_uncollapsed(self, real_tokens):
        exercises__scores = []
        for token in real_tokens:
            possible_exercises = token_to_exercise_name.get(token, [])
            for exercise_name in possible_exercises:
                score = float(len(token)) / len(exercise_name.replace("", " "))
                exercises__scores.append((exercise_name, score))
        return exercises__scores

    def _combined_exercise_scores(self, exercises__scores, num_tokens):
        collapsed_exercise_to_score = defaultdict(int)
        collapsed_exercise_to_occurence = defaultdict(int)
        for exercise, score in exercises__scores:
            collapsed_exercise_to_score[exercise] += score
            collapsed_exercise_to_occurence[exercise] += 1
        for exercise in list(collapsed_exercise_to_score.keys()):
            collapsed_exercise_to_score[exercise] *= collapsed_exercise_to_occurence[exercise] / float(num_tokens)
        return collapsed_exercise_to_score

    def _filtered_results(self, exercises__scores):
        min_results = 3
        max_results = 10
        score_threshold = 0.4
        max_possibles = exercises__scores[:max_results]
        if exercises__scores and exercises__scores[0][0] == 1.0:
            return [exercises__scores[0][0]]

        possibles_within_thresh = [tuple_obj for tuple_obj in exercises__scores if tuple_obj[1] >= score_threshold]
        min_possibles = possibles_within_thresh if len(possibles_within_thresh) > min_results else max_possibles[:min_results]
        return [tuple_obj[0] for tuple_obj in min_possibles]

    def guess_exercises(self, tokens):
        real_tokens = self._get_real_tokens_from_possible_n_grams(tokens)
        exercises__scores = self._get_scored_exercises_uncollapsed(real_tokens)
        collapsed_exercise_to_score = self_combined_exercise_scores(exercises__scores, len(tokens))
        exercises__scores = list(collapsed_exercise_to_score.items)
        exercises__scores.sort(key=lambda t: t[1], reverse=True)
        return self._filtered_results(exercises__scores)
