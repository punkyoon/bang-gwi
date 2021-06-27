from token import tokenize


if __name__ == '__main__':
    default_examples = [
        '뿡',
        '뿍뿍',
        '뽁뽁',
        '~',
        '뿌직',
        '쀼직',
        '뽀옹',
        '뽀뽀옹',
        '북',
        '부북',
        '부부북',
        '부부부북',
        '=3',
        '==3',
        '빵',
        '빠아앙',
    ]

    for idx, example in enumerate(examples):
        print(f'##### Test [{idx}] - {example}')
        result = tokenize(example)
        print(f'-> {result}')

    mix_example = '뿡뿍뿍뽁뽁~뿌직쀼직뽀옹뽀뽀옹북부북부부북부부부북=3==3빵빠아앙'

    print(f'###### Final Test - {mix_example}')
    result = tokenize(mix_example)
    print(f'-> {result}')
