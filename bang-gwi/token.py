from typing import List


def tokenize(code: str) -> List[str]:
    tokenized = []

    bbong_stack = []  # `뽀옹` | `뽀뽀옹`
    book_stack = []  # `북` | `부북` | `부부북` | `부부부북`
    bang_gwi_stack = []  # `=3` | `==3`
    bbook_stack = []  # `뿍뿍`
    bbok_stack = []  # `뽁뽁`
    bboozik_stack = []  # `뿌직`
    bbuzik_stack = []  # `쀼직`
    bbaang_stack = []  # `빠아앙`

    for op in code:
        if op  == '뽀':
            bbong_stack.append(op)
        elif op == '옹':
            bbong_stack.append(op)
            tokenized.append(''.join(bbong_stack))
            bbong_stack = []

        elif op == '뿍':
            bbook_stack.append(op)

            if len(bbook_stack) == 2:
                tokenized.append(''.join(bbook_stack))
                bbook_stack = []
                
        elif op == '뽁':
            bbok_stack.append(op)

            if len(bbok_stack) == 2:
                tokenized.append(''.join(bbok_stack))
                bbok_stack = []

        elif op == '뿌':
            bboozik_stack.append(op)
        elif op == '쀼':
            bbuzik_stack.append(op)
        elif op == '직':
            if '뿌' in bboozik_stack:
                bboozik_stack.append(op)
                tokenized.append(''.join(bboozik_stack))
                bboozik_stack = []
            elif '쀼' in bbuzik_stack:
                bbuzik_stack.append(op)
                tokenized.append(''.join(bbuzik_stack))
                bbuzik_stack = []

        elif op == '부':
            book_stack.append(op)
        elif op == '북':
            book_stack.append(op)
            tokenized.append(''.join(book_stack))
            book_stack = []
        
        elif op == '=':
            bang_gwi_stack.append(op)
        elif op == '3':
            bang_gwi_stack.append(op)
            tokenized.append(''.join(bang_gwi_stack))
            bang_gwi_stack = []

        elif op == '빠' or op == '아':
            bbaang_stack.append(op)
        elif op == '앙':
            bbaang_stack.append(op)
            tokenized.append(''.join(bbaang_stack))
            bbaang_stack = []

        else:
            tokenized.append(op)

    return tokenized
