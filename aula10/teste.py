from sys import stdin

texto = [
    "ajsdnjasnd asjdnasjdn 2, asdnajsdn",
    "sakdasd, 3 askpmdkasmd sdfdsf",
    "askdjasjd 1 asjdksad",
]

print(
    sorted(
        texto,
        key=lambda string: next(
            (
                word
                for word in [word.removesuffix(",") for word in string.split()]
                if word.isnumeric()
            ),
            None,
        ),
    )
)
