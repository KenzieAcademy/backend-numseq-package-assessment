## Overview - Creating Packages
In this assignment you will use TDD methodolgy to create several modules for computing various mathematical sequences.  The modules will then be grouped into a hierarchical package structure, with a top-level package name of `numseq`.  You will write tests first, then write code to pass the tests.

### `numseq`
Create a package folder named `numseq`, with the structure shown below.

Packages allow us organize and group modules (or python files). Python requires a specific structure for package definitions.
The directory name is the name of the package used in an import statement (`import package_name`). The submodules can be access as attributes of the package as in `package_name.submodule_name`.

```bash
├── numseq
│   ├── __init__.py
│   ├── fib.py
│   ├── geo.py
│   ├── prime.py
```

**`__init__.py`**

> The `__init__.py` files are required to make Python treat directories
> containing the file as packages. This prevents directories with a common
> name, such as string, unintentionally hiding valid modules that occur later
> on the module search path. In the simplest case, `__init__.py` can just be an
> empty file, but it can also execute initialization code for the package or
> set the `__all__` variable, described later.
>
> -- <cite>python docs</cite>

### `fib`
Within the numseq package, create a module named `fib.py`. Within the fib module, define a function `fib(n)` that returns the nth Fibonacci number.  The first 10 terms of the Fibonacci sequence are 
`[0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...]`

### `geo`
Within the numseq package, create a module named `geo.py`. Within this geo module, define 3 functions:
 - `square(n)` : Returns the nth term of the numbers that can be arranged into square geometric shapes `[1, 4, 9, 16, 25 ... ]`
 <br><img height="120px" src="https://i1.wp.com/www.stnicholasstlaurence.dorset.sch.uk/wp-content/uploads/2013/11/Square-Numbers.png" />

 - `triangle(n)` : Returns the nth term of the numbers that can be arranged in triangular geometric shapes `[1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... ]` 
 <br><img height="120px" src="https://www.101computing.net/wp/wp-content/uploads/trinagular-number-sequence.png" />

 - `cube(n)` : Returns the nth term of the numbers that can be arranged as symmetric cube shapes `[1, 8, 27, 64 ...]`
 <br><img height="180px" src="https://static.memrise.com/img/400sqf/from/uploads/course_photos/4974064000131215125138.gif" />

### `prime`
Finally, create a module named `prime.py` within the numseq package. Define the following functions:
 - `primes(n)`:  Returns a list of all prime numbers less than n
 - `is_prime(m)` : Returns a boolean indicating whether `m` is a prime number

## Testing
 - Use the VSCode built-in test discovery feature to run and debug individual tests
 - discover and run all tests

 >`$ python -m unittest discover`

 - run only one test

 >`$ python -m unittest test_numseq.TestNumseq.test_prime`


## PR (Pull Request) Workflow for this Assignment
1. *Fork* this repository into your own personal github account.
2. Then *Clone* your own repo to your local development machine.
3. Create a separate branch named `dev`, and checkout the branch.
5. Commit your changes, then `git push` the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your `dev` branch back to your own master.
6. Copy/Paste the URL **link to your PR** as your assignment submission.
7. Your grader will post code review comments inline with your code, in your github account. Be sure to respond to any comments and make requested changes. **RESUBMIT** a new link to your PR after making changes.  This is the code review iteration cycle.
