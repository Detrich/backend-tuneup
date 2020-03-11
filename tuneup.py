#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Detrich with help for Jordan davidson"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def profileDecorator(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args,**kwargs)
        pr.disable()
        ps = pstats.Stats(pr)
        ps.sort_stats('cumulative')
        ps.print_stats()
        return result
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    return profileDecorator


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    Moviez = {}
    duplicates = []
    for movie in movies:
        if movie not in Moviez:
            Moviez[movie] = 1
        else:
            Moviez[movie] +=1
    for movie in Moviez:
        if Moviez[movie] == 2:
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer("main()", "import tuneup")
    result = t.repeat(repeat=7, number=3)
    return 'best timing of 7 repeats of 3 runs per repeat: {} sec'.format(min(result) / 3)
#     # YOUR CODE GOES HERE


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    print(timeit_helper())
    


if __name__ == '__main__':
    main()
