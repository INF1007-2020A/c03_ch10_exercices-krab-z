#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    a=np.linspace(start=1.3, stop=2.5, num=64) 
    #a=(-1.3 + (2.5+13) * np.arange(0,64)/63) (the quickest way for short numbers, otherwise linspace)
    return a


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.argmin(abs(values-number))


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    a=np.linspace(-1.3,2.5,10)
    print(find_closest_index(a,1.1)
    print(a)
