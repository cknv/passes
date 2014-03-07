Passes
======

Passes is a small ulitiy to generate random passwords, or rather random strings out of a given set of characters. Which *can* be used as random passwords.

.. code-block:: bash
    $ passes
    Generating: 1
    Password length: 10
    Using charset: default
    0   =~@bPs73q:
    ...

The CLI was the original purpose of this utility, but an actual way of interacting with it has been added, making it possible to use Passes to make as a utility to generate random passwords.

.. code-block:: pycon

    >>> g = Generator()
    >>> g.generate()
    'Cel"UOdo>u'
    ...

Passes is in no way exceptional, and I believe any programmer with a decent knowledge of Python could crack out a similar (perhaps better) implementation within a short time.

As a final, disclaimer, I am in no way a security expert, but I do know that this implementation is subject to limitations in the random value generator of the platform it is running on, and that there may be all kinds of problems with the implementation. Generally I find it good enough to make me a random password, whenever I have the need for such.
