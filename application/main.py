import speedtest

def test():
    
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()

    res = s.results.dict()
    
    return res["download"], res["ping"]

def main():
    
    for i in range(5):
        print(f"Starting Test {i} ...")
        dowload_rate, ping = test()
        print(f"Finished Test {i}.")
        print(f"Results: {dowload_rate / 1028 / 1028:.2f} mb/s - {ping:.0f} ms")
        
        # TODO: Save res to csv with timestamp 
            
if __name__ == "__main__":
    main()