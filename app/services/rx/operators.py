from rx import pipe, from_list, empty, operators as ops


def cartesian_product():
    def cartesian(sources):
        if len(sources) == 0:
            return empty()

        result = sources[0].pipe(
            ops.map(lambda s: [s])
        )

        def two_streams_product(stream2, stream1):
            product = stream1.pipe(
                ops.flat_map(lambda s1: stream2.pipe(
                        ops.map(lambda s2: s1 + [s2])
                    )
                )
            )
            return product

        for i in range(1, len(sources)):
            result = two_streams_product(sources[i], result)

        return result

    return pipe(
        ops.map(lambda _list: from_list(_list)),
        ops.to_list(),
        ops.flat_map(lambda i: cartesian(i))
    )
