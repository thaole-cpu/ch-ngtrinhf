import json

# Đọc dữ liệu từ file JSON
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Lưu dữ liệu bài test vào file JSON
def save_test_results(results, file_path='test_results.json'):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

# Hàm thu thập thông tin người dùng
def collect_user_info():
    name = input("Nhập tên của bạn: ")
    age = input("Nhập tuổi của bạn: ")
    return name, age

# Hàm thực hiện bài test MBTI
def mbti_test():
    questions = [
        ("1. Bạn có xu hướng tập trung vào thực tế hơn là lý thuyết?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("2. Bạn cảm thấy thoải mái khi giao tiếp với người lạ?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("3. Bạn thường lập kế hoạch cụ thể trước khi thực hiện công việc?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("4. Bạn thích tìm hiểu và khám phá những ý tưởng mới?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("5. Bạn thích làm việc theo kế hoạch hơn là làm việc ngẫu hứng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("6. Bạn có xu hướng phân tích sự việc một cách logic và lý trí?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("7. Bạn thường dựa trên cảm xúc để ra quyết định?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("8. Bạn thích các hoạt động xã hội và thường chủ động giao tiếp với mọi người?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("9. Bạn có xu hướng hướng nội, thích ở một mình để suy ngẫm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("10. Bạn thích làm việc với dữ liệu và sự thật hơn là tưởng tượng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("11. Bạn cảm thấy thoải mái khi làm việc theo kế hoạch dài hạn?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("12. Bạn có xu hướng suy nghĩ về tương lai nhiều hơn hiện tại?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("13. Bạn thích ra quyết định nhanh chóng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("14. Bạn thích tìm hiểu sâu về một chủ đề cụ thể?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("15. Bạn thường quan tâm đến cảm xúc của người khác trong các quyết định của mình?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("16. Bạn có xu hướng quản lý thời gian chặt chẽ và kỷ luật?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("17. Bạn thích khám phá và thay đổi, hơn là duy trì mọi thứ như hiện tại?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("18. Bạn thường cảm thấy thoải mái khi làm việc dưới áp lực thời gian?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("19. Bạn thường cảm thấy kiên nhẫn trong các tình huống căng thẳng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("20. Bạn thích làm việc trong môi trường yên tĩnh, ít bị phân tâm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("21. Bạn thường lên kế hoạch chi tiết cho các hoạt động hàng ngày?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("22. Bạn thích có thời gian tự do để linh hoạt sáng tạo?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("23. Bạn có xu hướng đặt mục tiêu cụ thể và rõ ràng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("24. Bạn cảm thấy thoải mái khi đối mặt với những thay đổi đột ngột?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("25. Bạn thích thực hiện những kế hoạch lâu dài hơn là những công việc ngắn hạn?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("26. Bạn cảm thấy hứng thú khi giải quyết các vấn đề phức tạp?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("27. Bạn thường ưu tiên cho các hoạt động cá nhân hơn là nhóm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("28. Bạn cảm thấy dễ dàng làm việc theo nhóm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("29. Bạn có xu hướng tránh né những tình huống căng thẳng xã hội?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("30. Bạn thích học hỏi thông qua trải nghiệm thực tế?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("31. Bạn cảm thấy thoải mái khi làm việc với dữ liệu và phân tích?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("32. Bạn có xu hướng suy nghĩ chi tiết trước khi ra quyết định?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("33. Bạn cảm thấy hứng thú khi khám phá những ý tưởng mới lạ?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("34. Bạn có xu hướng suy nghĩ chiến lược khi đối mặt với các vấn đề?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("35. Bạn thích làm việc với các con số hơn là với con người?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("36. Bạn thích những công việc đòi hỏi sự chi tiết và tỉ mỉ?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("37. Bạn có xu hướng tự động điều chỉnh theo môi trường làm việc?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("38. Bạn thích dành thời gian suy nghĩ về ý tưởng trước khi thực hiện?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("39. Bạn cảm thấy thoải mái khi làm việc dưới thời gian gấp rút?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("40. Bạn thích các hoạt động yêu cầu sự sáng tạo và linh hoạt?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("41. Bạn thích lập kế hoạch mọi thứ từ trước thay vì hành động theo cảm hứng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("42. Bạn có xu hướng dễ thích nghi với những thay đổi trong cuộc sống?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("43. Bạn thích làm việc với các con số và phân tích số liệu?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("44. Bạn có xu hướng ưu tiên cảm xúc hơn là lý trí khi đưa ra quyết định?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("45. Bạn có xu hướng giữ im lặng trong những cuộc thảo luận nhóm?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("46. Bạn thích tìm hiểu về tương lai và những khả năng mới hơn là tập trung vào hiện tại?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("47. Bạn có xu hướng làm việc nhóm tốt hơn làm việc độc lập?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("48. Bạn thích xử lý các vấn đề dựa trên dữ liệu và sự kiện hơn là dựa trên cảm nhận?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),
        ("49. Bạn có xu hướng giải quyết các vấn đề theo trình tự rõ ràng?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý"),

        ("50. Bạn có xu hướng tránh rủi ro và luôn muốn an toàn trong công việc?",
         "a. Đồng ý hoàn toàn", "b. Đồng ý", "c. Không đồng ý", "d. Hoàn toàn không đồng ý")
    ]
    
    score = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
    
    for question in questions:
        answer = input(question + "\nNhập câu trả lời (a/b/c/d): ").strip().lower()
        
        while answer not in ['a', 'b', 'c', 'd']:
            answer = input("Câu trả lời không hợp lệ. Vui lòng nhập lại (a/b/c/d): ").strip().lower()
        
        # Cập nhật điểm số (cần điều chỉnh tùy theo cách tính MBTI)
        if question == questions[0]:
            if answer == 'a':
                score['E'] += 1
            else:
                score['I'] += 1
        elif question == questions[1]:
            if answer == 'a':
                score['F'] += 1
            else:
                score['T'] += 1
        elif question == questions[2]:
            if answer == 'a':
                score['J'] += 1
            else:
                score['P'] += 1

    mbti_type = ''.join([max(score, key=score.get) for _ in range(4)])  # Ví dụ đơn giản
    return mbti_type, score

# Hàm gợi ý ngành nghề phù hợp
def suggest_career(mbti_type, career_data):
    if mbti_type in career_data:
        return career_data[mbti_type]['Nghề nghiệp'], career_data[mbti_type]['Ngành học']
    return [], []

# Hàm lọc trường đại học
def filter_universities(universities, selected_majors, min_tuition, max_tuition, region):
    filtered_universities = []
    for university in universities:
        if region in university['Khu vực'] and any(major in university['Ngành học'] for major in selected_majors):
            tuition = university['Học phí']
            if (tuition.startswith('<') and float(tuition[1:]) < max_tuition) or \
               (tuition.startswith('>') and float(tuition[1:]) > min_tuition) or \
               (tuition.isdigit() and min_tuition <= float(tuition) <= max_tuition) or \
               (tuition == '-'):
                filtered_universities.append(university['Tên trường'])
    return filtered_universities

def main():
    # Tải dữ liệu
    career_data = load_data('data1.json')
    universities = load_data('data2.json')

    # Thu thập thông tin người dùng
    name, age = collect_user_info()

    # Thực hiện bài test MBTI
    mbti_type, score = mbti_test()
    print(f"Kiểu MBTI của bạn là: {mbti_type}")

    # Gợi ý ngành nghề và ngành học cụ thể
    suitable_industries, suitable_majors = suggest_career(mbti_type, career_data)
    
    print("Nhóm ngành nghề phù hợp:")
    for industry in suitable_industries:
        print(f"- {industry}")

    print("Ngành học cụ thể phù hợp:")
    for major in suitable_majors:
        print(f"- {major}")

    # Nhập học phí và khu vực
    min_tuition = float(input("Nhập học phí tối thiểu: "))
    max_tuition = float(input("Nhập học phí tối đa: "))
    region = input("Nhập khu vực (Bắc, Trung, Nam): ")

    # Lọc danh sách trường đại học theo ngành học cụ thể
    filtered_universities = filter_universities(universities, suitable_majors, min_tuition, max_tuition, region)

    # Hiển thị danh sách trường đại học phù hợp
    print("Danh sách trường đại học phù hợp:")
    for university in filtered_universities:
        print(f"- {university}")

    # Lưu kết quả bài test
    test_results = {
        'name': name,
        'age': age,
        'mbti_type': mbti_type,
        'score': score,
        'suitable_industries': suitable_industries,
        'suitable_majors': suitable_majors,
        'filtered_universities': filtered_universities
    }
    
    save_test_results(test_results)

if __name__ == "__main__":
    main()