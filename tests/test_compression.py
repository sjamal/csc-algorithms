"""Comprehensive evaluation suite tracking Huffman Coding compression operations."""

import pytest
from src.compression.huffman import encode, decode


def test_huffman_round_trip_typical_text():
    """Verifies that encoding followed by decoding recovers the original text exactly."""
    text = "abracadabra"
    encoded_bits, codebook = encode(text)

    assert decode(encoded_bits, codebook) == text

    # More frequent characters should never receive a longer code than rarer ones
    assert len(codebook["a"]) <= len(codebook["r"])


def test_huffman_compression_efficiency():
    """Confirms the encoded bitstring is shorter than a naive fixed-width encoding."""
    text = "aaaaabbbccd"
    encoded_bits, _ = encode(text)

    naive_fixed_width_bits = len(text) * 8
    assert len(encoded_bits) < naive_fixed_width_bits


def test_huffman_single_unique_character():
    """Ensures a text composed of one repeated character still yields a valid one-bit code."""
    text = "zzzzz"
    encoded_bits, codebook = encode(text)

    assert codebook == {"z": "0"}
    assert encoded_bits == "00000"
    assert decode(encoded_bits, codebook) == text


def test_huffman_empty_text():
    """Ensures empty input is handled gracefully without raising an exception."""
    encoded_bits, codebook = encode("")

    assert encoded_bits == ""
    assert codebook == {}
    assert decode(encoded_bits, codebook) == ""


def test_huffman_decode_invalid_bitstream():
    """Ensures a malformed bitstring not matching any known code raises a ValueError."""
    codebook = {"a": "01", "b": "10", "c": "11"}

    # A lone leading bit can never resolve to any of these fixed 2-bit codewords
    with pytest.raises(ValueError, match="not a valid sequence"):
        decode("0", codebook)


def test_huffman_decode_duplicate_codebook_rejected():
    """Ensures a malicious/malformed codebook with duplicate codes is rejected safely."""
    malicious_codebook = {"a": "0", "b": "0"}

    with pytest.raises(ValueError, match="duplicate codes"):
        decode("00", malicious_codebook)
