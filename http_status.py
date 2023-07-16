from enum import Enum
from typing import Optional, Union


class HTTPStatus(Enum):
    """
    Enumerates common HTTP Status codes with meaningful names as described by the
    Mozilla Developer Network documentation here:
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    """
    # informational
    HTTP_100 = (100, "Continue")
    HTTP_101 = (101, "Switching Protocols")
    HTTP_102 = (102, "Processing")
    HTTP_103 = (103, "Early Hints")

    # successful
    HTTP_200 = (200, "Ok")
    HTTP_201 = (201, "Created")
    HTTP_202 = (202, "Accepted")
    HTTP_203 = (203, "Non-Authoritative Information")
    HTTP_204 = (204, "No Content")
    HTTP_205 = (205, "Reset Content")
    HTTP_206 = (206, "Partial Content")
    HTTP_207 = (207, "Multi-Status")
    HTTP_208 = (208, "Already Reported")
    HTTP_226 = (226, "IM Used")

    # redirection
    HTTP_300 = (300, "Multiple Choices")
    HTTP_301 = (301, "Moved Permanently")
    HTTP_302 = (302, "Found")
    HTTP_303 = (303, "See Other")
    HTTP_304 = (304, "Not Modified")
    HTTP_305 = (305, "Use Proxy")
    HTTP_306 = (306, "Unused")
    HTTP_307 = (307, "Temporary Redirect")
    HTTP_308 = (308, "Permanent Redirect")

    # client errors
    HTTP_400 = (400, "Bad Request")
    HTTP_401 = (401, "Unauthorized")
    HTTP_402 = (402, "Payment Required")
    HTTP_403 = (403, "Forbidden")
    HTTP_404 = (404, "Not Found")
    HTTP_405 = (405, "Method Not Allowed")
    HTTP_406 = (406, "Not Acceptable")
    HTTP_407 = (407, "Proxy Authentication Required")
    HTTP_408 = (408, "Request Timeout")
    HTTP_409 = (409, "Conflict")
    HTTP_410 = (410, "Gone")
    HTTP_411 = (411, "Length Required")
    HTTP_412 = (412, "Precondition Failed")
    HTTP_413 = (413, "Payload Too Large")
    HTTP_415 = (415, "Unsupported Media Type")
    HTTP_416 = (416, "Range Not Satisfiable")
    HTTP_417 = (417, "Expectation Failed")
    HTTP_418 = (418, "I'm A Teapot")
    HTTP_421 = (421, "Misdirected Request")
    HTTP_422 = (422, "Unprocessable Content")
    HTTP_423 = (423, "Locked")
    HTTP_424 = (424, "Failed Dependency")
    HTTP_425 = (425, "Too Early")
    HTTP_426 = (426, "Upgrade Required")
    HTTP_428 = (428, "Precondition Required")
    HTTP_429 = (429, "Too Many Requests")
    HTTP_431 = (431, "Request Header Fields Too Large")
    HTTP_451 = (451, "Unavailable For Legal Reasons")

    # server errors
    HTTP_500 = (500, "Internal Server Error")
    HTTP_501 = (501, "Not Implemented")
    HTTP_502 = (502, "Bad Gateway")
    HTTP_503 = (503, "Service Unavailable")
    HTTP_504 = (504, "Gateway Timeout")
    HTTP_505 = (505, "HTTP Version Not Supported")
    HTTP_506 = (506, "Variant Also Negotiates")
    HTTP_507 = (507, "Insufficient Storage")
    HTTP_508 = (508, "Loop Detected")
    HTTP_510 = (510, "Not Extended")
    HTTP_511 = (511, "Network Authorization Required")

    def __str__(self) -> str:
        """
        Represents HTTP Status objects in a string format as such:
            HTTP <code>: <description>
        """
        return f"HTTP {self.value[0]}: {self.value[1]}"

    def __eq__(self, other):
        """
        Compares values directly to the code
        """
        if isinstance(other, HTTPStatus):
            return self.code() == other.code()
        if not isinstance(other, (int, float)):
            return False
        return self.code() == other

    def __gt__(self, other):
        """
        Compares values directly to code
        """
        if isinstance(other, HTTPStatus):
            return self.code() < other.code()
        if not isinstance(other, (int, float)):
            return False
        return self.code() > other

    def __ge__(self, other):
        return self == other or self > other

    def __lt__(self, other):
        return not self > other and self != other

    def __le__(self, other):
        return self < other or self == other

    def code(self) -> int:
        """
        Returns the numerical code associated with the HTTP Status object.
        """
        return self.value[0]

    def desc(self) -> str:
        """
        Returns the string description of the HTTP Status object.
        """
        return self.value[1]

    @staticmethod
    def get_from_code(code: int) -> Optional["HTTPStatus"]:
        """
        Returns an HTTP Status object associated with a numeric code.
        """
        for status in HTTPStatus:
            if status.code() == code:
                return status
        return None
