# Copyright (c) 2020 Anastasiia Birillo, Elena Lyulina

import logging

from src.test.test_util import LoggedTest
from src.main.util.consts import LOGGER_NAME, TASK
from src.main.util.file_util import get_content_from_file
from src.test.canonicalization.canonicalization.util import run_test, CANONIZATION_TESTS_TYPES
from src.main.canonicalization.canonicalization import get_cleaned_code, anonymize_names, get_ast, get_code_from_tree,\
    get_canonicalized_form

log = logging.getLogger(LOGGER_NAME)


def get_cleaned_code_from_file(file: str) -> str:
    source = get_content_from_file(file)
    return get_cleaned_code(source).rstrip('\n')


def get_code_with_anonymous_names(file: str) -> str:
    source = get_cleaned_code_from_file(file)
    tree = get_ast(source)
    actual_code = get_code_from_tree(anonymize_names(tree)).rstrip('\n')
    return actual_code


def get_canonicalized_code(file: str) -> str:
    source = get_content_from_file(file)
    return get_code_from_tree(get_canonicalized_form(source)).rstrip('\n')


class TestCanonicalizationTool(LoggedTest):

    def test_cleaned_code(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.CLEANED_CODE, get_cleaned_code_from_file)

    def test_anonymize_names(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.ANONYMIZE_NAMES, get_code_with_anonymous_names)

    def test_canonical_form(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.CANONICAL_FORM, get_canonicalized_code)

    def test_student_code_pies(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.STUDENT_CODE, get_canonicalized_code, TASK.PIES)

    def test_student_code_max_3(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.STUDENT_CODE, get_canonicalized_code, TASK.MAX_3)

    def test_student_code_is_zero(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.STUDENT_CODE, get_canonicalized_code, TASK.ZERO)

    def test_student_code_max_digit(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.STUDENT_CODE, get_canonicalized_code, TASK.MAX_DIGIT)

    def test_student_code_election(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.STUDENT_CODE, get_canonicalized_code, TASK.ELECTION)

    def test_student_code_brackets(self) -> None:
        run_test(self, CANONIZATION_TESTS_TYPES.STUDENT_CODE, get_canonicalized_code, TASK.BRACKETS)
