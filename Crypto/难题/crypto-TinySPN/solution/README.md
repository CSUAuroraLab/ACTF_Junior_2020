# solution

## TL;DR

attack simple SPN by chosen-plaintext attack, use linear cryptanalysis or differential cryptanalysis will break it. [exp](exp.py) use linear cryptanalysis.

## Detail

because this SPN cipher is so simple, so we just need following steps.

1. get LAT, like [example](lat.py)(Linear Approximation Table).
2. find one path with high bias.
3. collecting enough plaintext-cipher pairs.
4. extracting key from pairs.(check exp for more details).([linear_cryptanalysis.py](linear_cryptanalysis.py) is a example of this step, but code is like a shit so you'd better forget it.)
5. decrypt flag.

[test.py](test.py) is my test data, ignore it.

if SBOX is so good that can't break it, record it and replay exp~

[send me](mailto:CSUwangj@protonmail.com) this SBOX so that I can post it~