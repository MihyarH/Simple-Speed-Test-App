from speedtest import Speedtest

Internet = Speedtest()

print("Getting your download speed ...")
Download = Internet.download()
print(f"Your Download Speed : {Download / 1024 / 1024:.2f} mbps")

print("Getting your upload speed ...")
Upload = Internet.upload()
print(f"Your Upload Speed : {Upload / 1024 / 1024:.2f} mbps")
