def coding_is_a_physical_education_subject(N):
    answer = ["long"] * (N // 4) 
    answer += ["int"]
    
    return " ".join(answer)


if __name__ == "__main__":
    N = int(input())
    
    print(coding_is_a_physical_education_subject(N))