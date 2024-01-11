from concurrent.futures import ThreadPoolExecutor


def get_data_concurrently(function, cpu_threads_amount) -> list:
    with ThreadPoolExecutor(max_workers=cpu_threads_amount) as executor:
        future_to_ordinal = {
            executor.submit(function, ordinal, cpu_threads_amount): ordinal
            for ordinal in range(cpu_threads_amount)
        }

        data = []
        for future in future_to_ordinal:
            data += future.result()

    return data
