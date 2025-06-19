import io
import struct
import xled

# discovered_device = xled.discover.discover()
# discovered_device.id

# control = xled.ControlInterface(discovered_device.ip_address, discovered_device.hw_address)


def make_solid_movie(num, r, g, b):
    pat = [struct.pack(">BBB", r, g, b)] * num
    print(pat)
    movie = io.BytesIO()
    movie.write(b"".join(pat))
    movie.seek(0)
    return movie

if __name__ == "__main__":
    movie_file = make_solid_movie(10, 255, 125, 0)
    print(movie_file)

    with open("output.txt", "wb") as f:
        f.write(movie_file.getbuffer())
