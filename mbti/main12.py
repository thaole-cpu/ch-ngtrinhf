import json

# Đọc dữ liệu nghề nghiệp và trường học từ file JSON
with open("D:\\nhom1\mbti\data1.json", "r", encoding="utf-8") as f:
    job_data = json.load(f)

with open("D:\\nhom1\mbti\data2.json", "r", encoding="utf-8") as f:
    school_data = json.load(f)

# Hàm thực hiện bài test MBTI
def mbti_test():
    questions = [(1, "Tại một buổi tiệc, bạn sẽ:", "a. Giao tiếp với nhiều người, kể cả người lạ", "b. Chỉ giao tiếp với một số ít người mà bạn đã quen", "E", "I"),
        (2, "Bạn thấy mình là người nghiêng về kiểu nào nhiều hơn?", "a. Thực tế", "b. Sáng tạo", "S", "N"),
        (3, "Bạn nghĩ tình huống nào tồi tệ hơn?", "a. Đầu óc của bạn cứ 'bay bổng trên mây'", "b. Cuộc sống của bạn thật nhàm chán và không bao giờ thay đổi", "N", "S"),
        (4, "Bạn sẽ bị ấn tượng hơn với:", "a. Các nguyên tắc", "b. Những cảm xúc", "T", "F"),
        (5, "Khi quyết định việc gì đó, bạn thường dựa vào:", "a. Sự thuyết phục", "b. Sự đồng cảm", "T", "F"),
        (6, "Bạn thích làm việc theo kiểu nào nhiều hơn?", "a. Theo đúng thời hạn", "b. Tùy hứng", "J", "P"),
        (7, "Bạn có khuynh hướng đưa ra các lựa chọn:", "a. Rất cẩn thận", "b. Phần nào theo cảm nhận", "J", "P"),
        (8, "Tại các bữa tiệc, bạn thường:", "a. Ở lại tới cùng và cảm thấy càng lúc càng hào hứng", "b. Ra về sớm vì cảm thấy mệt mỏi dần", "E", "I"),
        (9, "Kiểu người nào sẽ thu hút bạn hơn?", "a. Người thực tế và có lý lẽ", "b. Người giàu trí tưởng tượng", "S", "N"),
        (10, "Điều nào khiến bạn thấy thích thú hơn?", "a. Những điều thực tế", "b. Những ý tưởng khả thi", "S", "N"),
        (11, "Khi đánh giá người khác, bạn dựa vào điều gì?", "a. Luật lệ và nguyên tắc", "b. Hoàn cảnh", "T", "F"),
        (12, "Khi tiếp xúc người khác, bạn nghiêng về hướng nào?", "a. Khách quan", "b. Trải nghiệm cá nhân", "T", "F"),
        (13, "Phong cách của bạn nghiêng về hướng nào hơn?", "a. Đúng giờ, nghiêm túc", "b. Nhàn nhã, thoải mái", "J", "P"),
        (14, "Bạn cảm thấy không thoải mái khi có những việc:", "a. Chưa hoàn thiện", "b. Đã quá hoàn thiện", "J", "P"),
        (15, "Trong các mối quan hệ xã hội, bạn thường:", "a. Nắm bắt kịp thông tin của mọi người", "b. Biết thông tin sau người khác", "E", "I"),
        (16, "Với các công việc thông thường, bạn nghiêng về cách:", "a. Làm theo cách thông thường", "b. Làm theo cách của riêng mình", "S", "N"),
        (17, "Các nhà văn nên:", "a. Viết những gì họ nghĩ", "b. Dùng sự so sánh, liên tưởng", "S", "N"),
        (18, "Điều gì lôi cuốn bạn hơn?", "a. Tính nhất quán", "b. Sự hòa hợp trong quan hệ", "T", "F"),
        (19, "Bạn cảm thấy thoải mái hơn khi đưa ra:", "a. Những đánh giá logic", "b. Những đánh giá có ý nghĩa", "T", "F"),
        (20, "Bạn thích những điều:", "a. Đã sắp xếp, quyết định trước", "b. Chưa xác định", "J", "P"),
        (21, "Bạn tự thấy mình:", "a. Nghiêm túc, quyết đoán", "b. Dễ gần, thoải mái", "J", "P"),
        (22, "Khi nói chuyện điện thoại, bạn:", "a. Cứ gọi bình thường", "b. Chuẩn bị trước điều sẽ nói", "E", "I"),
        (23, "Những sự kiện thực tế:", "a. Tự giải thích", "b. Giải thích cho quy tắc", "S", "N"),
        (24, "Người có tầm nhìn xa:", "a. Gây khó chịu cho người khác", "b. Thú vị", "S", "N"),
        (25, "Bạn thường là người:", "a. Cái đầu lạnh", "b. Trái tim nóng", "T", "F"),
        (26, "Điều nào tồi tệ hơn?", "a. Không công bằng", "b. Tàn nhẫn", "T", "F"),
        (27, "Sự kiện nên xảy ra theo hướng:", "a. Được lựa chọn kỹ", "b. Ngẫu nhiên", "J", "P"),
        (28, "Bạn cảm thấy thoải mái khi:", "a. Đã mua xong", "b. Đang lựa chọn để mua", "J", "P"),
        (29, "Trong công ty, bạn là người:", "a. Khởi xướng câu chuyện", "b. Đợi người khác bắt chuyện", "E", "I"),
        (30, "Đối với quy tắc xã hội, bạn:", "a. Ít khi nghi ngờ", "b. Thường xem xét lại", "S", "N"),
        (31, "Trẻ em thường:", "a. Chưa cố gắng đủ", "b. Chưa vui chơi đủ", "T", "F"),
        (32, "Khi đưa ra quyết định, bạn thoải mái hơn với:", "a. Các tiêu chuẩn", "b. Cảm xúc", "T", "F"),
        (33, "Bạn nghiêng về tính cách nào hơn?", "a. Cứng rắn", "b. Nhẹ nhàng", "T", "F"),
        (34, "Khả năng nào đáng khâm phục hơn?", "a. Tổ chức, phương pháp", "b. Thích ứng, xoay xở", "J", "P"),
        (35, "Bạn đề cao tố chất nào hơn?", "a. Sự chắc chắn", "b. Sự cởi mở", "J", "P"),
        (36, "Khi tương tác với người khác trong tình huống mới:", "a. Phấn chấn", "b. Mệt mỏi", "E", "I"),
        (37, "Thường thì bạn là:", "a. Người thực tế", "b. Người tưởng tượng phong phú", "S", "N"),
        (38, "Bạn thường có xu hướng:", "a. Xem người khác làm gì hữu ích", "b. Xem người khác nghĩ gì", "T", "F"),
        (39, "Bạn cảm thấy thoải mái hơn khi:", "a. Thảo luận vấn đề triệt để", "b. Đạt được thỏa thuận", "T", "F"),
        (40, "Cái đầu hay trái tim chi phối bạn nhiều hơn?", "a. Cái đầu", "b. Trái tim", "T", "F"),
        (41, "Bạn thích làm việc theo kiểu:", "a. Giao trọn gói, làm xong rồi bàn giao", "b. Công việc hàng ngày", "J", "P"),
        (42, "Bạn có xu hướng tìm kiếm:", "a. Theo trật tự", "b. Ngẫu nhiên", "J", "P"),
        (43, "Bạn thích kiểu nào hơn?", "a. Nhiều bạn bè xã giao", "b. Một vài bạn thân", "E", "I"),
        (44, "Bạn thường dựa vào:", "a. Sự kiện thực tế", "b. Nguyên lý", "S", "N"),
        (45, "Bạn hứng thú với việc gì hơn?", "a. Sản xuất và phân phối", "b. Thiết kế và nghiên cứu", "S", "N"),
        (46, "Lời khen nào giá trị hơn?", "a. Người có suy nghĩ logic", "b. Người tình cảm, tinh tế", "T", "F"),
        (47, "Bạn thích mình có tố chất nào hơn?", "a. Kiên định, vững vàng", "b. Toàn tâm, cống hiến", "T", "F"),
        (48, "Bạn thích điều nào hơn?", "a. Một tuyên bố cuối cùng", "b. Một tuyên bố dự kiến", "J", "P"),
        (49, "Bạn thấy thoải mái hơn vào lúc:", "a. Trước khi đưa ra quyết định", "b. Sau khi đưa ra quyết định", "J", "P"),
        (50, "Bạn có thấy mình:", "a. Dễ bắt chuyện với người mới", "b. Khó trò chuyện với người mới", "E", "I"),
        (51, "Bạn có xu hướng tin vào:", "a. Kinh nghiệm", "b. Linh cảm", "S", "N"),
        (52, "Bạn cho rằng mình là người:", "a. Thực tế", "b. Khôn khéo", "T", "F"),
        (53, "Ai là người đáng khen hơn?", "a. Người lý trí", "b. Người cảm xúc", "T", "F"),
        (54, "Bạn có xu hướng hành xử:", "a. Công bằng, vô tư", "b. Thông cảm, đồng cảm", "T", "F"),
        (55, "Bạn thích:", "a. Đảm bảo mọi việc được chuẩn bị sẵn", "b. Để mọi việc diễn ra tự nhiên", "J", "P"),
        (56, "Trong các mối quan hệ, mọi việc:", "a. Có thể thảo luận để giải quyết", "b. Diễn ra ngẫu nhiên tùy hoàn cảnh", "J", "P"),
        (57, "Khi chuông điện thoại reo, bạn:", "a. Là người đầu tiên nhấc máy", "b. Hy vọng người khác sẽ nhấc máy", "E", "I"),
        (58, "Bạn đánh giá cao điều gì hơn?", "a. Nhận thức thực tế", "b. Trí tưởng tượng phong phú", "S", "N"),
        (59, "Bạn chú tâm hơn đến:", "a. Nguyên tắc cơ bản", "b. Ngụ ý, ẩn ý", "T", "F"),
        (60, "Điều gì có vẻ là lỗi lớn hơn?", "a. Quá nồng nhiệt, thiết tha", "b. Quá khách quan, thờ ơ", "T", "F"),
        (61, "Về cơ bản, bạn tự thấy mình là người:", "a. Thiết thực, ít bị tình cảm chi phối", "b. Từ tâm, đa cảm", "T", "F"),
        (62, "Tình huống nào lôi cuốn bạn hơn?", "a. Tình huống rõ ràng, có kế hoạch", "b. Tình huống không xác định", "J", "P"),
        (63, "Bạn là người có xu hướng nào hơn?", "a. Theo thói quen", "b. Hay thay đổi", "J", "P"),
        (64, "Bạn có xu hướng nào hơn?", "a. Dễ tiếp cận", "b. Kín đáo ở mức nào đó", "E", "I"),
        (65, "Khi viết, bạn thích:", "a. Viết theo hướng văn chương", "b. Viết theo số liệu, dữ liệu", "S", "N"),
        (66, "Điều gì khó thực hiện hơn đối với bạn?", "a. Hiểu và chia sẻ với người khác", "b. Điều khiển người khác", "T", "F"),
        (67, "Bạn mong ước mình sẽ có thêm điều gì?", "a. Lý trí, khả năng phán đoán rõ ràng", "b. Tình thương, lòng trắc ẩn sâu sắc", "T", "F"),
        (68, "Điều gì sẽ là lỗi lớn hơn?", "a. Hành động bừa bãi, không cân nhắc", "b. Chỉ trích, phê phán", "T", "F"),
        (69, "Bạn thích sự kiện nào hơn?", "a. Có kế hoạch trước", "b. Không có kế hoạch trước", "J", "P"),
        (70, "Bạn thường có hành động:", "a. Cân nhắc thận trọng", "b. Tự nhiên, tự phát", "J", "P")
    
        
    ]

    scores = {
        "E": 0, "I": 0, "S": 0, "N": 0,
        "T": 0, "F": 0, "J": 0, "P": 0
    }

    for idx, (question, opt1, opt2) in enumerate(questions, start=1):
        print(f"Câu {idx}: {question}")
        print(opt1)
        print(opt2)
        answer = input("Chọn đáp án (a/b): ").strip().lower()
        
        if answer == 'a':
            if "(I)" in opt1: scores["I"] += 1
            elif "(S)" in opt1: scores["S"] += 1
            elif "(T)" in opt1: scores["T"] += 1
            elif "(J)" in opt1: scores["J"] += 1
        elif answer == 'b':
            if "(E)" in opt2: scores["E"] += 1
            elif "(N)" in opt2: scores["N"] += 1
            elif "(F)" in opt2: scores["F"] += 1
            elif "(P)" in opt2: scores["P"] += 1

    # Xác định loại MBTI từ điểm số
    mbti_type = (
        "E" if scores["E"] > scores["I"] else "I" +
        "S" if scores["S"] > scores["N"] else "N" +
        "T" if scores["T"] > scores["F"] else "F" +
        "J" if scores["J"] > scores["P"] else "P"
    )

    return mbti_type

# Hàm tìm nghề nghiệp phù hợp theo loại MBTI
def find_job_by_mbti(mbti_type):
    jobs = []
    for job in job_data:
        if mbti_type in job["mbti_type"]:
            jobs.append(job["industries"])
    return jobs

# Hàm tìm trường học phù hợp dựa trên học phí và khu vực
def find_school(max_tuition, region):
    suitable_schools = []
    for school in school_data:
        tuition = school["tuition"].replace(" ", "").replace(">", "").replace("<", "").replace("-", "").split("đến")
        min_tuition = int(tuition[0])
        max_tuition_in_data = int(tuition[1]) if len(tuition) > 1 else min_tuition
        
        if min_tuition <= max_tuition and school["region"].lower() == region.lower():
            suitable_schools.append(school["name"])
    return suitable_schools

# Hàm định hướng nghề nghiệp
def career_guidance():
    name = input("Nhập tên của bạn: ")
    age = input("Nhập tuổi của bạn: ")
    max_tuition = int(input("Nhập giới hạn học phí (số cụ thể, ví dụ: 20000000): "))
    region = input("Khu vực mong muốn (Bắc, Trung, Nam): ")
    
    # Lấy loại MBTI từ bài kiểm tra
    mbti_type = mbti_test()
    print(f"\nKết quả MBTI của bạn là: {mbti_type}")
    
    # Tìm nghề nghiệp phù hợp
    jobs = find_job_by_mbti(mbti_type)
    if not jobs:
        print("Không tìm thấy ngành nghề phù hợp với loại MBTI của bạn.")
    else:
        print("Ngành nghề phù hợp với bạn:")
        for job in jobs:
            print(f"- {job}")

    # Tìm trường học phù hợp
    schools = find_school(max_tuition, region)
    if not schools:
        print("Không tìm thấy trường đại học phù hợp với yêu cầu của bạn.")
    else:
        print("\nCác trường đại học phù hợp với bạn:")
        for school in schools:
            print(f"- {school}")

    # Lưu kết quả vào file
    user_data = {
        "name": name,
        "age": age,
        "mbti_type": mbti_type,
        "jobs": jobs,
        "schools": schools
    }

    with open("D:\\nhom1\mbti\\test_results.json", "a", encoding="utf-8") as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)
        f.write(",\n")

# Chạy chương trình
career_guidance()