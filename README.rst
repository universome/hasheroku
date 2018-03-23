hasheroku
============

Traditional hashing seems boring and mundane?
Can't bear the heartlessness of their musty hex strings?
Put down the razor: we have something for you.

.. code:: python

    hasheroku('Hashing goes bananas!')    # -> 'throbbing-mountain'
    hasheroku('Hashing goes bananas.')    # -> 'summer-frost'
    hasheroku('Hasheroku goes bananas!')  # -> 'withered-star'
    hasheroku('Everything goes bananas!') # -> 'icy-thunder'

:code:`hasheroku` hashes strings into nice hashes, using heroku naming conventions.
It's like a heroku random names `generator`_, but hashing function!

**DISCLAIMER**: There are only 64x64 = 4096 unique combinations of heroku names, so *there will be a whole lot of collisions*.
That's why never use bare heroku hashes (i.e. without hex suffixes — explained `below`_) in the situations, where you are going to generate a lot of hashes!

.. _generator : https://github.com/usmanbashir/haikunator
.. _below : https://github.com/universome/hasheroku#usage

Installation
============
You can install :code:`hasheroku` using :code:`pip`:

.. code:: bash

    pip install hasheroku

Usage
============
If you are not going to hash a lot of strings and/or do not care about collisions, than you can use it in a standard way:

.. code:: python

    hasheroku('I love hashes!') # -> 'old-fiesta'

You can use your own separator with :code:`separator` argument:

.. code:: python

    hasheroku('I love hashes!', separator='~')          # -> 'old~fiesta'
    hasheroku('Maaan, who does not like hashes?!', ' ') # -> 'lingering shadow'

If you are really serious and responsible about your hashing and would like to avoid collisions, then you can append part of the hash from the :code:`sha256` digest to the produced heroku hash.
This can be done with an optional :code:`suffix_len` argument:

.. code:: python

    hasheroku('I love hashes!', suffix_len=5)               # -> 'old-fiesta-cd298'
    hasheroku('I love hashes!', 10, '~')                    # -> 'old~fiesta~cd29895f2a'
    hasheroku('Maaan, who does not like hashes?!', 30, ' ') # -> 'lingering shadow a7c1c6cd56a755c3e87d9b667ef9dd'

In this case, of course, you lose all the awesomeness of human-readable hashes and can just use traditional hashing functions.

Are all names equally likely to be generated?
============
Yes. First, we get sha256 hash of the string, than we project its first 4 hexadecimal characters into heroku adjectives and names.
As long as these 4 characters are uniformly distributed (and they do) and we project them properly (and we do) — our hashes are uniformly distributed too.
The problem, of course, is with the tiny amount of possible names, that's why we have a lot of collisions.

Man, why?
============
This project can be useful when you regurarly deploy services/run experiments and want their names to be a hash of their config file.
Using traditional hashing like md5/sha256 makes the names look ugly and their large entropy is not needed at all in such a case.

Contributing and TODOs
============

.. |ss| raw:: html

   <strike>

.. |se| raw:: html

   </strike>

If you feel like you have nothing else to do with your life, you can contribute to this project.
It will be cool to make the following things:

* Write a proper test for uniformity. There is a Kolmogorov-Smirnov test to check if a random variable is uniform, but it works only with continuous variables. And I do not know how to check the same thing for discrete ones (friendly, I didn't google this much, because I was a little bit |ss| lazy |se| busy).
* Add more names and adjectives. This will allow us to reduce amount of collisions. Currently, I've hardcoded usage of only 64 adjectives/names. To sample properly I suppose we should take binary digest of the sha256 and use `this`_.

.. _this : https://stats.stackexchange.com/questions/70073/generating-discrete-uniform-from-coin-flips
