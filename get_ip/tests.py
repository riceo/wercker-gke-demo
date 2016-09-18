from webtest import TestApp

import get_ip


def test_functional_get_ip():
    """Set a fake IP and check we get it as a response"""

    app = TestApp(get_ip.app)

    test_ip = "1.2.3.4"

    # Set the client's IP address for our test case
    extra_environ = dict(REMOTE_ADDR=test_ip)

    # Make a get request to our app
    resp = app.get('/', extra_environ=extra_environ)

    # test that the body of the response contains
    # the IP address we set above.
    resp.mustcontain(test_ip)

    # Test that we got a successful HTTP response code
    assert resp.status == "200 OK"
