import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    jokes = []
    for i in range(count):
        random_noun = random.choice(nouns)
        random_adverb = random.choice(adverbs)
        random_adjective = random.choice(adjectives)
        joke = f"{random_noun} {random_adverb} {random_adjective}"
        jokes.append(joke)
    return jokes


def get_jokes_adv(count: int, are_repeats_allowed: bool) -> list:
    if are_repeats_allowed:
        return get_jokes(count)
    else:
        random_nouns = nouns.copy()
        random_adverbs = adverbs.copy()
        random_adjectives = adjectives.copy()

        random.shuffle(random_nouns)
        random.shuffle(random_adverbs)
        random.shuffle(random_adjectives)

        jokes = zip(random_nouns, random_adverbs, random_adjectives)
        jokes = map(lambda joke: ' '.join(joke), jokes)

        return list(jokes)[0:count]


kwargs = {
    "count": 12,
    "are_repeats_allowed": False,
}
print(get_jokes_adv(**kwargs))
