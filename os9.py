def fifo(page_references, num_frames):
    page_faults = 0
    frames = []
    replace_index = 0  # Index to track the position to replace
    print("\nFIFO Page Replacement Algorithm:")
    print(f"{'Page':<10}{'Added':<10}{'Removed':<10}{'Page Fault':<12}{'Frame Content'}")
    print("-" * 60)

    for page in page_references:
        if page not in frames:
            page_faults += 1
            if len(frames) == num_frames:
                removed_page = frames[replace_index]
                frames[replace_index] = page
                replace_index = (replace_index + 1) % num_frames  # Update replace index
                print(f"{page:<10}{page:<10}{removed_page:<10}{'Yes':<12}{frames}")
            else:
                frames.append(page)
                print(f"{page:<10}{page:<10}{'-':<10}{'Yes':<12}{frames}")
        else:
            print(f"{page:<10}{'-':<10}{'-':<10}{'No':<12}{frames}")

    print(f"\nTotal Page Faults (FIFO): {page_faults}\n")
    return page_faults


def OPT(frames, pages):
    page_faults = 0
    page_frame = []

    print("\nOPT (Optimal Page Replacement) Algorithm:")
    print(f"{'Page':<10}{'Added':<10}{'Removed':<10}{'Page Fault':<12}{'Frame Content'}")
    print("-" * 60)

    for page_index in range(len(pages)):
        page = pages[page_index]

        if page not in page_frame:
            page_faults += 1
            if len(page_frame) < frames:
                page_frame.append(page)
                print(f"{page:<10}{page:<10}{'-':<10}{'Yes':<12}{page_frame}")
            else:
                future_pages = pages[page_index:]
                farthest = -1
                farthest_page = None

                for frame in page_frame:
                    try:
                        index = future_pages.index(frame)
                        if index > farthest:
                            farthest = index
                            farthest_page = frame
                    except ValueError:
                        farthest = len(future_pages)
                        farthest_page = frame
                        break

                page_frame[page_frame.index(farthest_page)] = page
                print(f"{page:<10}{page:<10}{farthest_page:<10}{'Yes':<12}{page_frame}")

        else:
            print(f"{page:<10}{'-':<10}{'-':<10}{'No':<12}{page_frame}")

    print(f"\nTotal Page Faults (OPT): {page_faults}\n")
    return page_faults


def LRU(frames, pages):
    page_faults = 0
    page_frame = []
    page_order = []

    print("\nLRU (Least Recently Used) Algorithm:")
    print(f"{'Page':<10}{'Added':<10}{'Removed':<10}{'Page Fault':<12}{'Frame Content'}")
    print("-" * 60)

    for page in pages:
        if page not in page_frame:
            page_faults += 1
            if len(page_frame) < frames:
                page_frame.append(page)
                page_order.append(page)
                print(f"{page:<10}{page:<10}{'-':<10}{'Yes':<12}{page_frame}")
            else:
                least_recently_used = page_order.pop(0)
                page_frame[page_frame.index(least_recently_used)] = page
                page_order.append(page)
                print(f"{page:<10}{page:<10}{least_recently_used:<10}{'Yes':<12}{page_frame}")

        else:
            page_order.remove(page)
            page_order.append(page)
            print(f"{page:<10}{'-':<10}{'-':<10}{'No':<12}{page_frame}")

    print(f"\nTotal Page Faults (LRU): {page_faults}\n")
    return page_faults


def main():
    frames = int(input("Enter the number of frames: "))
    pages = list(map(int, input("Enter the page reference sequence separated by spaces: ").split()))

    fifo_faults = fifo(pages, frames)
    opt_faults = OPT(frames, pages)
    lru_faults = LRU(frames, pages)

    print("\nSummary of Page Faults:")
    print(f"{'Algorithm':<10}{'Total Page Faults'}")
    print("-" * 30)
    print(f"{'FIFO':<10}{fifo_faults}")
    print(f"{'OPT':<10}{opt_faults}")
    print(f"{'LRU':<10}{lru_faults}\n")


if __name__ == "__main__":
    main()
