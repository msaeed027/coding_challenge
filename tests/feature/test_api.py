import pytest
import json


@pytest.mark.parametrize(
    ('combination_type', 'request_payload', 'expected_response'),
    [
        ('', None, {'error': 'Payload must be a valid json.'}),
        ('', [], {'error': 'Request should contains list of lists (at least one list represents the products).'}),
        ('', [[]], {'error': 'Request should contains list of lists which first list should include at least one product.'}),

        ('py', [['a']], [['a']]),
        ('', [['a', 'b']], [['a'], ['b']]),
        ('', [['a', 'b'], [1, 2]], [['a', 1], ['a', 2], ['b', 1], ['b', 2]]),

        ('custom', [['a']], [['a']]),
        ('custom', [['a', 'b']], [['a'], ['b']]),
        ('custom', [['a', 'b'], [1, 2]], [['a', 1], ['a', 2], ['b', 1], ['b', 2]]),

        ('rx', [['a']], [['a']]),
        ('rx', [['a', 'b']], [['a'], ['b']]),
        ('rx', [['a', 'b'], [1, 2]], [['a', 1], ['a', 2], ['b', 1], ['b', 2]]),
    ]
)
def test_combine(client, combination_type, request_payload, expected_response):
    query_string = f'?combination_type={combination_type}' if combination_type else ''
    url = f'api/combine{query_string}'
    request_payload = json.dumps(request_payload) if isinstance(request_payload, list) else ''
    response = client.post(url, data=request_payload, headers={'Content-Type': 'application/json'})

    response_data = json.loads(response.data)

    if isinstance(response_data, dict) and 'error' in response_data:  # error because success responses is type of list
        assert response.status_code == 400  # i only have validation with dict response and status_code 400
    else:
        assert response.status_code == 200

    assert response_data == expected_response
