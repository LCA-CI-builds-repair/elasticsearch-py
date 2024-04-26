#  Licensed to Elasticsearch B.V. under one or more contributor
class TestTransformError:
    def test_transform_error_parse_with_error_reason(self):
        e = ApiError(
            message="InternalServerError",
            meta=error_meta,
            body={
                "error": {"root_cause": [{"type": "error", "reason": "error reason"}]}
            },
        )

        assert e.status == 500
        assert e.reason == "error reason"
        assert str(e) == "ApiError(500, 'InternalServerError', 'error reason')"

    def test_transform_error_parse_with_error_string(self):
        e = ApiError(
            message="InternalServerError",
            meta=error_meta,
            body={"error": "something error message"},
        )

        assert e.status == 500
        assert e.reason == "something error message"
        assert (
            str(e) == "ApiError(500, 'InternalServerError', 'something error message')"
        )