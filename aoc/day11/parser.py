def parse_devices(input_text: str) -> dict[str, list[str]]:
    """Parse input into adjacency list representing device connections.

    Args:
        input_text: Raw input with lines like "device: output1 output2"

    Returns:
        Dict mapping device name to list of output device names
    """
    graph = {}
    for line in input_text.strip().split('\n'):
        if not line.strip():
            continue
        device, outputs = line.split(': ')
        graph[device] = outputs.split()
    return graph
