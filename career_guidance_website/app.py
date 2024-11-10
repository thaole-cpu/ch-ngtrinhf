from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

# Hàm tải dữ liệu từ JSON
def load_data():
    with open('D:\\nhom1-6\\data1.json', 'r', encoding='utf-8') as f:
        career_data = json.load(f)
    with open('D:\\nhom1-6\\data2.json', 'r', encoding='utf-8') as f:
        school_data = json.load(f)
    return career_data, school_data

# Hàm lưu kết quả vào file JSON
def save_test_results(result):
    with open('D:\\nhom1-6\\test_results.json', 'a', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)
        f.write("\n")

# Các hàm hỗ trợ khác như calculate_mbti, find_careers, find_majors...
# Hàm xử lý học phí
def parse_tuition(tuition_str):
    # Xử lý trường hợp học phí là 0 hoặc chuỗi trống
    if tuition_str == 0 or tuition_str == "0" or tuition_str.strip() == "":
        return (0, 0)
    
    # Loại bỏ các ký tự không cần thiết
    tuition_str = tuition_str.replace(",", "").strip()
    
    try:
        if ">" in tuition_str:
            # Trường hợp chuỗi bắt đầu với ">"
            return int(tuition_str.replace(">", "").strip()), float('inf')
        
        elif "<" in tuition_str:
            # Trường hợp chuỗi bắt đầu với "<"
            return 0, int(tuition_str.replace("<", "").strip())
        
        elif "-" in tuition_str:
            # Trường hợp chuỗi có khoảng giá "low-high"
            low, high = map(int, tuition_str.split('-'))
            return low, high
        
        else:
            # Trường hợp chuỗi là một giá trị duy nhất
            value = int(tuition_str)
            return value, value
    
    except ValueError:
        # Xử lý lỗi nếu chuỗi không thể chuyển đổi thành số
        print(f"Warning: Unable to parse tuition value from '{tuition_str}'. Defaulting to (0, 0).")
        return (0, 0)  # Hoặc giá trị mặc định khác nếu phù hợp
 
# Hàm lọc trường theo học phí
def filter_school_by_tuition(school_data, max_tuition):
    filtered_schools = []
    for school in school_data:
        # Gọi hàm parse_tuition để lấy giá trị học phí tối thiểu và tối đa
        min_tuition, max_tuition_in_data = parse_tuition(school["tuition"])

        # Bỏ qua trường có học phí bằng 0 (không hợp lệ)
        if min_tuition == 0 and max_tuition_in_data == 0:
            continue

        # Kiểm tra điều kiện lọc học phí
        if min_tuition <= max_tuition and max_tuition_in_data <= max_tuition:
            filtered_schools.append(school)
    
    return filtered_schools


# Lọc trường học theo khu vực
def filter_school_by_region(school_data, region):
    region = f"Miền {region.capitalize()}"
    return [school for school in school_data if school["region"] == region]

# Lọc trường học theo ngành học
def filter_school_by_major(school_data, majors):
    filtered_schools = []
    for school in school_data:
        school_majors = school.get("majors", [])
        if any(major in school_majors for major in majors):
            filtered_schools.append(school)
    return filtered_schools
# Tìm ngành nghề theo MBTI (chỉ hiển thị mỗi industry một lần)
def find_careers(mbti_type, career_data):
    unique_industries = set()
    careers = []
    for career in career_data:
        if mbti_type in career["mbti_type"].split(", "):
            industry = career["industries"]
            if industry not in unique_industries:
                unique_industries.add(industry)
                careers.append(industry)
    return careers
def find_majors(mbti_type, major_data):
    unique_majors = set()
    majors = []
    for major in major_data:
        if mbti_type in major["mbti_type"].split(", "):
            major_name = major["majors"]
            if major_name not in unique_majors:
                unique_majors.add(major_name)
                majors.append(major_name)
    return majors
# Hàm tính toán MBTI từ câu trả lời bài kiểm tra
def calculate_mbti(answers):
    questions = [
               ( "Tại một buổi tiệc, bạn sẽ:", "a. Giao tiếp với nhiều người, kể cả người lạ", "b. Chỉ giao tiếp với một số ít người mà bạn đã quen"),
        ( "Bạn thấy mình là người nghiêng về kiểu nào nhiều hơn?", "a. Thực tế", "b. Sáng tạo"),
        ( "Bạn nghĩ tình huống nào tồi tệ hơn?", "a. Đầu óc của bạn cứ 'bay bổng trên mây'", "b. Cuộc sống của bạn thật nhàm chán và không bao giờ thay đổi"),
        ( "Bạn sẽ bị ấn tượng hơn với:", "a. Các nguyên tắc", "b. Những cảm xúc"),
        ( "Khi quyết định việc gì đó, bạn thường dựa vào:", "a. Sự thuyết phục", "b. Sự đồng cảm"),
        ( "Bạn thích làm việc theo kiểu nào nhiều hơn?", "a. Theo đúng thời hạn", "b. Tùy hứng"),
        ( "Bạn có khuynh hướng đưa ra các lựa chọn:", "a. Rất cẩn thận", "b. Phần nào theo cảm nhận"),
        ("Tại các bữa tiệc, bạn thường:", "a. Ở lại tới cùng và cảm thấy càng lúc càng hào hứng", "b. Ra về sớm vì cảm thấy mệt mỏi dần"),
        ("Kiểu người nào sẽ thu hút bạn hơn?", "a. Người thực tế và có lý lẽ", "b. Người giàu trí tưởng tượng"),
        ( "Điều nào khiến bạn thấy thích thú hơn?", "a. Những điều thực tế", "b. Những ý tưởng khả thi"),
        ( "Khi đánh giá người khác, bạn dựa vào điều gì?", "a. Luật lệ và nguyên tắc", "b. Hoàn cảnh"),
        ( "Khi tiếp xúc người khác, bạn nghiêng về hướng nào?", "a. Khách quan", "b. Trải nghiệm cá nhân"),
        ( "Phong cách của bạn nghiêng về hướng nào hơn?", "a. Đúng giờ, nghiêm túc", "b. Nhàn nhã, thoải mái"),
        ( "Bạn cảm thấy không thoải mái khi có những việc:", "a. Chưa hoàn thiện", "b. Đã quá hoàn thiện"),
        ( "Trong các mối quan hệ xã hội, bạn thường:", "a. Nắm bắt kịp thông tin của mọi người", "b. Biết thông tin sau người khác"),
        ( "Với các công việc thông thường, bạn nghiêng về cách:", "a. Làm theo cách thông thường", "b. Làm theo cách của riêng mình"),
        ( "Các nhà văn nên:", "a. Viết những gì họ nghĩ", "b. Dùng sự so sánh, liên tưởng"),
        ( "Điều gì lôi cuốn bạn hơn?", "a. Tính nhất quán", "b. Sự hòa hợp trong quan hệ"),
        ( "Bạn cảm thấy thoải mái hơn khi đưa ra:", "a. Những đánh giá logic", "b. Những đánh giá có ý nghĩa"),
        ( "Bạn thích những điều:", "a. Đã sắp xếp, quyết định trước", "b. Chưa xác định"),
        ( "Bạn tự thấy mình:", "a. Nghiêm túc, quyết đoán", "b. Dễ gần, thoải mái"),
        ( "Khi nói chuyện điện thoại, bạn:", "a. Cứ gọi bình thường", "b. Chuẩn bị trước điều sẽ nói"),
        ( "Những sự kiện thực tế:", "a. Tự giải thích", "b. Giải thích cho quy tắc"),
        ( "Người có tầm nhìn xa:", "a. Gây khó chịu cho người khác", "b. Thú vị"),
        ( "Bạn thường là người:", "a. Cái đầu lạnh", "b. Trái tim nóng"),
        ( "Điều nào tồi tệ hơn?", "a. Không công bằng", "b. Tàn nhẫn"),
        ( "Sự kiện nên xảy ra theo hướng:", "a. Được lựa chọn kỹ", "b. Ngẫu nhiên"),
        ( "Bạn cảm thấy thoải mái khi:", "a. Đã mua xong", "b. Đang lựa chọn để mua"),
        ( "Trong công ty, bạn là người:", "a. Khởi xướng câu chuyện", "b. Đợi người khác bắt chuyện"),
        ( "Đối với quy tắc xã hội, bạn:", "a. Ít khi nghi ngờ", "b. Thường xem xét lại"),
        ( "Trẻ em thường:", "a. Chưa cố gắng đủ", "b. Chưa vui chơi đủ"),
        ( "Khi đưa ra quyết định, bạn thoải mái hơn với:", "a. Các tiêu chuẩn", "b. Cảm xúc"),
        ( "Bạn nghiêng về tính cách nào hơn?", "a. Cứng rắn", "b. Nhẹ nhàng"),
        ( "Khả năng nào đáng khâm phục hơn?", "a. Tổ chức, phương pháp", "b. Thích ứng, xoay xở"),
        ( "Bạn đề cao tố chất nào hơn?", "a. Sự chắc chắn", "b. Sự cởi mở"),
        ( "Khi tương tác với người khác trong tình huống mới:", "a. Phấn chấn", "b. Mệt mỏi"),
        ( "Thường thì bạn là:", "a. Người thực tế", "b. Người tưởng tượng phong phú"),
        ( "Bạn thường có xu hướng:", "a. Xem người khác làm gì hữu ích", "b. Xem người khác nghĩ gì"),
        ( "Bạn cảm thấy thoải mái hơn khi:", "a. Thảo luận vấn đề triệt để", "b. Đạt được thỏa thuận"),
        ( "Cái đầu hay trái tim chi phối bạn nhiều hơn?", "a. Cái đầu", "b. Trái tim"),
        ( "Bạn thích làm việc theo kiểu:", "a. Giao trọn gói, làm xong rồi bàn giao", "b. Công việc hàng ngày"),
        ( "Bạn có xu hướng tìm kiếm:", "a. Theo trật tự", "b. Ngẫu nhiên"),
        ( "Bạn thích kiểu nào hơn?", "a. Nhiều bạn bè xã giao", "b. Một vài bạn thân"),
        ( "Bạn thường dựa vào:", "a. Sự kiện thực tế", "b. Nguyên lý"),
        ( "Bạn hứng thú với việc gì hơn?", "a. Sản xuất và phân phối", "b. Thiết kế và nghiên cứu"),
        ( "Lời khen nào giá trị hơn?", "a. Người có suy nghĩ logic", "b. Người tình cảm, tinh tế"),
        ( "Bạn thích mình có tố chất nào hơn?", "a. Kiên định, vững vàng", "b. Toàn tâm, cống hiến"),
        ( "Bạn thích điều nào hơn?", "a. Một tuyên bố cuối cùng", "b. Một tuyên bố dự kiến"),
        ("Bạn thấy thoải mái hơn vào lúc:", "a. Trước khi đưa ra quyết định", "b. Sau khi đưa ra quyết định"),
        ("Bạn có thấy mình:", "a. Dễ bắt chuyện với người mới", "b. Khó trò chuyện với người mới"),
        ( "Bạn có xu hướng tin vào:", "a. Kinh nghiệm", "b. Linh cảm"),
        ( "Bạn cho rằng mình là người:", "a. Thực tế", "b. Khôn khéo"),
        ( "Ai là người đáng khen hơn?", "a. Người lý trí", "b. Người cảm xúc"),
        ( "Bạn có xu hướng hành xử:", "a. Công bằng, vô tư", "b. Thông cảm, đồng cảm"),
        ( "Bạn thích:", "a. Đảm bảo mọi việc được chuẩn bị sẵn", "b. Để mọi việc diễn ra tự nhiên"),
        ( "Trong các mối quan hệ, mọi việc:", "a. Có thể thảo luận để giải quyết", "b. Diễn ra ngẫu nhiên tùy hoàn cảnh"),
        ( "Khi chuông điện thoại reo, bạn:", "a. Là người đầu tiên nhấc máy", "b. Hy vọng người khác sẽ nhấc máy"),
        ( "Bạn đánh giá cao điều gì hơn?", "a. Nhận thức thực tế", "b. Trí tưởng tượng phong phú"),
        ( "Bạn chú tâm hơn đến:", "a. Nguyên tắc cơ bản", "b. Ngụ ý, ẩn ý"),
        ( "Điều gì có vẻ là lỗi lớn hơn?", "a. Quá nồng nhiệt, thiết tha", "b. Quá khách quan, thờ ơ"),
        ( "Về cơ bản, bạn tự thấy mình là người:", "a. Thiết thực, ít bị tình cảm chi phối", "b. Từ tâm, đa cảm"),
        ( "Tình huống nào lôi cuốn bạn hơn?", "a. Tình huống rõ ràng, có kế hoạch", "b. Tình huống không xác định"),
        ( "Bạn là người có xu hướng nào hơn?", "a. Theo thói quen", "b. Hay thay đổi"),
        ( "Bạn có xu hướng nào hơn?", "a. Dễ tiếp cận", "b. Kín đáo ở mức nào đó"),
        ( "Khi viết, bạn thích:", "a. Viết theo hướng văn chương", "b. Viết theo số liệu, dữ liệu"),
        ( "Điều gì khó thực hiện hơn đối với bạn?", "a. Hiểu và chia sẻ với người khác", "b. Điều khiển người khác"),
        ( "Bạn mong ước mình sẽ có thêm điều gì?", "a. Lý trí, khả năng phán đoán rõ ràng", "b. Tình thương, lòng trắc ẩn sâu sắc"),
        ( "Điều gì sẽ là lỗi lớn hơn?", "a. Hành động bừa bãi, không cân nhắc", "b. Chỉ trích, phê phán"),
        ( "Bạn thích sự kiện nào hơn?", "a. Có kế hoạch trước", "b. Không có kế hoạch trước"),
        ( "Bạn thường có hành động:", "a. Cân nhắc thận trọng", "b. Tự nhiên, tự phát")
    ]
    scores = {
        "E": 0, "I": 0,
        "S": 0, "N": 0,
        "T": 0, "F": 0,
        "J": 0, "P": 0
    }

    for idx, (question, opt1, opt2) in enumerate(questions, start=1):
        print(f"Câu {idx}: {question}")
        print(opt1)
        print(opt2)
        # neu dap an khong hop le
        while True:
            answer = input("Chọn đáp án (a/b): ").strip().lower()
            if answer in ['a', 'b']:
                  break
            else:
                 print("Vui lòng chỉ chọn đáp án 'a' hoặc 'b'.")

        # Cộng điểm cho từng loại MBTI
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
        ("E" if scores["E"] > scores["I"] else "I") +
        ("S" if scores["S"] > scores["N"] else "N") +
        ("T" if scores["T"] > scores["F"] else "F") +
        ("J" if scores["J"] > scores["P"] else "P")
    )

    return mbti_type

# Hàm định hướng nghề nghiệp
def career_guidance(name, age, mbti_type, max_tuition, region):
    career_data, school_data = load_data()
    careers = find_careers(mbti_type, career_data)
    majors = find_majors(mbti_type, career_data)
    schools_by_tuition = filter_school_by_tuition(school_data, max_tuition)
    schools_by_region = filter_school_by_region(schools_by_tuition, region)
    suitable_schools = filter_school_by_major(schools_by_region, majors)

    # Chuẩn bị kết quả để lưu
    result = {
        "name": name,
        "age": age,
        "mbti_type": mbti_type,
        "careers": careers,
        "majors": majors,
        "suitable_schools": suitable_schools,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_test_results(result)  # Lưu kết quả vào JSON
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mbti_test', methods=['GET', 'POST'])
def mbti_test():
    questions = [
               ( "Tại một buổi tiệc, bạn sẽ:", "a. Giao tiếp với nhiều người, kể cả người lạ", "b. Chỉ giao tiếp với một số ít người mà bạn đã quen"),
        ( "Bạn thấy mình là người nghiêng về kiểu nào nhiều hơn?", "a. Thực tế", "b. Sáng tạo"),
        ( "Bạn nghĩ tình huống nào tồi tệ hơn?", "a. Đầu óc của bạn cứ 'bay bổng trên mây'", "b. Cuộc sống của bạn thật nhàm chán và không bao giờ thay đổi"),
        ( "Bạn sẽ bị ấn tượng hơn với:", "a. Các nguyên tắc", "b. Những cảm xúc"),
        ( "Khi quyết định việc gì đó, bạn thường dựa vào:", "a. Sự thuyết phục", "b. Sự đồng cảm"),
        ( "Bạn thích làm việc theo kiểu nào nhiều hơn?", "a. Theo đúng thời hạn", "b. Tùy hứng"),
        ( "Bạn có khuynh hướng đưa ra các lựa chọn:", "a. Rất cẩn thận", "b. Phần nào theo cảm nhận"),
        ("Tại các bữa tiệc, bạn thường:", "a. Ở lại tới cùng và cảm thấy càng lúc càng hào hứng", "b. Ra về sớm vì cảm thấy mệt mỏi dần"),
        ("Kiểu người nào sẽ thu hút bạn hơn?", "a. Người thực tế và có lý lẽ", "b. Người giàu trí tưởng tượng"),
        ( "Điều nào khiến bạn thấy thích thú hơn?", "a. Những điều thực tế", "b. Những ý tưởng khả thi"),
        ( "Khi đánh giá người khác, bạn dựa vào điều gì?", "a. Luật lệ và nguyên tắc", "b. Hoàn cảnh"),
        ( "Khi tiếp xúc người khác, bạn nghiêng về hướng nào?", "a. Khách quan", "b. Trải nghiệm cá nhân"),
        ( "Phong cách của bạn nghiêng về hướng nào hơn?", "a. Đúng giờ, nghiêm túc", "b. Nhàn nhã, thoải mái"),
        ( "Bạn cảm thấy không thoải mái khi có những việc:", "a. Chưa hoàn thiện", "b. Đã quá hoàn thiện"),
        ( "Trong các mối quan hệ xã hội, bạn thường:", "a. Nắm bắt kịp thông tin của mọi người", "b. Biết thông tin sau người khác"),
        ( "Với các công việc thông thường, bạn nghiêng về cách:", "a. Làm theo cách thông thường", "b. Làm theo cách của riêng mình"),
        ( "Các nhà văn nên:", "a. Viết những gì họ nghĩ", "b. Dùng sự so sánh, liên tưởng"),
        ( "Điều gì lôi cuốn bạn hơn?", "a. Tính nhất quán", "b. Sự hòa hợp trong quan hệ"),
        ( "Bạn cảm thấy thoải mái hơn khi đưa ra:", "a. Những đánh giá logic", "b. Những đánh giá có ý nghĩa"),
        ( "Bạn thích những điều:", "a. Đã sắp xếp, quyết định trước", "b. Chưa xác định"),
        ( "Bạn tự thấy mình:", "a. Nghiêm túc, quyết đoán", "b. Dễ gần, thoải mái"),
        ( "Khi nói chuyện điện thoại, bạn:", "a. Cứ gọi bình thường", "b. Chuẩn bị trước điều sẽ nói"),
        ( "Những sự kiện thực tế:", "a. Tự giải thích", "b. Giải thích cho quy tắc"),
        ( "Người có tầm nhìn xa:", "a. Gây khó chịu cho người khác", "b. Thú vị"),
        ( "Bạn thường là người:", "a. Cái đầu lạnh", "b. Trái tim nóng"),
        ( "Điều nào tồi tệ hơn?", "a. Không công bằng", "b. Tàn nhẫn"),
        ( "Sự kiện nên xảy ra theo hướng:", "a. Được lựa chọn kỹ", "b. Ngẫu nhiên"),
        ( "Bạn cảm thấy thoải mái khi:", "a. Đã mua xong", "b. Đang lựa chọn để mua"),
        ( "Trong công ty, bạn là người:", "a. Khởi xướng câu chuyện", "b. Đợi người khác bắt chuyện"),
        ( "Đối với quy tắc xã hội, bạn:", "a. Ít khi nghi ngờ", "b. Thường xem xét lại"),
        ( "Trẻ em thường:", "a. Chưa cố gắng đủ", "b. Chưa vui chơi đủ"),
        ( "Khi đưa ra quyết định, bạn thoải mái hơn với:", "a. Các tiêu chuẩn", "b. Cảm xúc"),
        ( "Bạn nghiêng về tính cách nào hơn?", "a. Cứng rắn", "b. Nhẹ nhàng"),
        ( "Khả năng nào đáng khâm phục hơn?", "a. Tổ chức, phương pháp", "b. Thích ứng, xoay xở"),
        ( "Bạn đề cao tố chất nào hơn?", "a. Sự chắc chắn", "b. Sự cởi mở"),
        ( "Khi tương tác với người khác trong tình huống mới:", "a. Phấn chấn", "b. Mệt mỏi"),
        ( "Thường thì bạn là:", "a. Người thực tế", "b. Người tưởng tượng phong phú"),
        ( "Bạn thường có xu hướng:", "a. Xem người khác làm gì hữu ích", "b. Xem người khác nghĩ gì"),
        ( "Bạn cảm thấy thoải mái hơn khi:", "a. Thảo luận vấn đề triệt để", "b. Đạt được thỏa thuận"),
        ( "Cái đầu hay trái tim chi phối bạn nhiều hơn?", "a. Cái đầu", "b. Trái tim"),
        ( "Bạn thích làm việc theo kiểu:", "a. Giao trọn gói, làm xong rồi bàn giao", "b. Công việc hàng ngày"),
        ( "Bạn có xu hướng tìm kiếm:", "a. Theo trật tự", "b. Ngẫu nhiên"),
        ( "Bạn thích kiểu nào hơn?", "a. Nhiều bạn bè xã giao", "b. Một vài bạn thân"),
        ( "Bạn thường dựa vào:", "a. Sự kiện thực tế", "b. Nguyên lý"),
        ( "Bạn hứng thú với việc gì hơn?", "a. Sản xuất và phân phối", "b. Thiết kế và nghiên cứu"),
        ( "Lời khen nào giá trị hơn?", "a. Người có suy nghĩ logic", "b. Người tình cảm, tinh tế"),
        ( "Bạn thích mình có tố chất nào hơn?", "a. Kiên định, vững vàng", "b. Toàn tâm, cống hiến"),
        ( "Bạn thích điều nào hơn?", "a. Một tuyên bố cuối cùng", "b. Một tuyên bố dự kiến"),
        ("Bạn thấy thoải mái hơn vào lúc:", "a. Trước khi đưa ra quyết định", "b. Sau khi đưa ra quyết định"),
        ("Bạn có thấy mình:", "a. Dễ bắt chuyện với người mới", "b. Khó trò chuyện với người mới"),
        ( "Bạn có xu hướng tin vào:", "a. Kinh nghiệm", "b. Linh cảm"),
        ( "Bạn cho rằng mình là người:", "a. Thực tế", "b. Khôn khéo"),
        ( "Ai là người đáng khen hơn?", "a. Người lý trí", "b. Người cảm xúc"),
        ( "Bạn có xu hướng hành xử:", "a. Công bằng, vô tư", "b. Thông cảm, đồng cảm"),
        ( "Bạn thích:", "a. Đảm bảo mọi việc được chuẩn bị sẵn", "b. Để mọi việc diễn ra tự nhiên"),
        ( "Trong các mối quan hệ, mọi việc:", "a. Có thể thảo luận để giải quyết", "b. Diễn ra ngẫu nhiên tùy hoàn cảnh"),
        ( "Khi chuông điện thoại reo, bạn:", "a. Là người đầu tiên nhấc máy", "b. Hy vọng người khác sẽ nhấc máy"),
        ( "Bạn đánh giá cao điều gì hơn?", "a. Nhận thức thực tế", "b. Trí tưởng tượng phong phú"),
        ( "Bạn chú tâm hơn đến:", "a. Nguyên tắc cơ bản", "b. Ngụ ý, ẩn ý"),
        ( "Điều gì có vẻ là lỗi lớn hơn?", "a. Quá nồng nhiệt, thiết tha", "b. Quá khách quan, thờ ơ"),
        ( "Về cơ bản, bạn tự thấy mình là người:", "a. Thiết thực, ít bị tình cảm chi phối", "b. Từ tâm, đa cảm"),
        ( "Tình huống nào lôi cuốn bạn hơn?", "a. Tình huống rõ ràng, có kế hoạch", "b. Tình huống không xác định"),
        ( "Bạn là người có xu hướng nào hơn?", "a. Theo thói quen", "b. Hay thay đổi"),
        ( "Bạn có xu hướng nào hơn?", "a. Dễ tiếp cận", "b. Kín đáo ở mức nào đó"),
        ( "Khi viết, bạn thích:", "a. Viết theo hướng văn chương", "b. Viết theo số liệu, dữ liệu"),
        ( "Điều gì khó thực hiện hơn đối với bạn?", "a. Hiểu và chia sẻ với người khác", "b. Điều khiển người khác"),
        ( "Bạn mong ước mình sẽ có thêm điều gì?", "a. Lý trí, khả năng phán đoán rõ ràng", "b. Tình thương, lòng trắc ẩn sâu sắc"),
        ( "Điều gì sẽ là lỗi lớn hơn?", "a. Hành động bừa bãi, không cân nhắc", "b. Chỉ trích, phê phán"),
        ( "Bạn thích sự kiện nào hơn?", "a. Có kế hoạch trước", "b. Không có kế hoạch trước"),
        ( "Bạn thường có hành động:", "a. Cân nhắc thận trọng", "b. Tự nhiên, tự phát")
    ]
    if request.method == 'POST':
        answers = [request.form.get(f'answer_{i}') for i in range(len(questions))]
        mbti_type = calculate_mbti(answers)
        name = request.form.get('name')
        age = request.form.get('age')
        
        return redirect(url_for('submit', mbti_type=mbti_type, name=name, age=age))
    return render_template('mbti_test.html', questions=questions)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.args.get('name')
        age = request.args.get('age')
        mbti_type = request.args.get('mbti_type')
        max_tuition = int(request.form['tuition'])
        region = request.form['region']
        
        # Tìm kiếm định hướng nghề nghiệp và lưu kết quả
        result = career_guidance(name, age, mbti_type, max_tuition, region)

        # Hiển thị kết quả
        return render_template(
            'result.html',
            name=result["name"],
            age=result["age"],
            mbti_type=result["mbti_type"],
            careers=result["careers"],
            majors=result["majors"],
            suitable_schools=result["suitable_schools"]
        )
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)