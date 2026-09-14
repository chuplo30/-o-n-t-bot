import os


dong_vat = ["chó","mèo","voi","hổ","rắn","cá","gà","vịt","heo","bò","trâu","ngựa","dê","cừu","khỉ","gấu","thỏ","chuột","sư tử","báo","hươu","nai","cáo","sói","hạc","đại bàng","chim","cú","bướm","ong","kiến","muỗi","ruồi","gián","nhện","bọ cạp","tôm","cua","ốc","mực","bạch tuộc","cá sấu","rùa","ếch","nhái","thằn lằn","tắc kè","kỳ đà","hải cẩu","cá voi","cá heo","chim ưng","bồ câu","yến","thiên nga","ngỗng","vẹt","đà điểu","khủng long","sứa","sao biển","hà mã","tê giác","hươu cao cổ","linh cẩu","sóc","nhím","mối","mọt","châu chấu","chuồn chuồn","bọ ngựa","bọ xít","đom đóm","cá mập","cá ngựa","cá hồi","cá rô","cá chép","cá vàng","cá trê","cá lóc","cá basa","gà trống","gà mái","gà con","vịt xiêm","vịt trời","ngan","công","trĩ","gà tây","chó sói","chó ngao","chó poodle","mèo tam thể","mèo mun","mèo mướp","mèo Ba Tư","khỉ đột","tinh tinh","đười ươi","gấu trúc","gấu bắc cực","gấu nâu","cáo tuyết","sư tử biển","hải mã","cá đuối","cá kiếm","cá ngừ","cá thu","cá chỉ vàng","cá cảnh","cá diêu hồng","cá lia thia","cá betta","cá la hán","cá rồng","cá đĩa","cá tỳ bà","cá chuột","cá mún","cá bảy màu","tép","tôm hùm","tôm sú","tôm càng","ghẹ","hàu","nghêu","sò","trai","bào ngư","hải sâm","nhum","mực ống","mực nang","bạch tuộc đốm","sao biển đỏ","san hô","huệ biển","hải quỳ"]

do_vat = ["bàn","ghế","quạt","tivi","điện thoại","máy tính","tủ","giường","gối","chăn","màn","ly","cốc","chén","bát","đĩa","muỗng","thìa","nĩa","đũa","nồi","chảo","mâm","rổ","bao","túi","bóp","ví","cặp","nón","mũ","áo","quần","váy","khăn","nhẫn","đồng hồ","gương","lược","kéo","dao","búa","đinh","chìa khóa","ổ khóa","ô","dù","chổi","thau","xô","máy giặt","tủ lạnh","máy lạnh","lò vi sóng","bếp","xe đạp","xe máy","ô tô","tàu thủy","máy bay","bút","thước","tập","sách","vở","đèn","pin","sạc","tai nghe","loa","micro","camera","máy ảnh","bóng đèn","quạt trần","điều hòa","nồi cơm","ấm siêu tốc","bàn ủi","máy hút bụi","máy sấy","máy xay","máy ép","nồi chiên","lò nướng","bếp ga","bếp từ","chén trà","ly nước","bình hoa","chậu cây","thảm","rèm","cửa","cửa sổ","cầu thang","ban công","sân","tường","mái nhà","gạch","ngói","xi măng","cát","đá","gỗ","sắt","thép","nhôm","đồng","chì","kẽm","vàng","bạc","bạch kim","kim cương","đá quý","ngọc trai","san hô","hổ phách","pha lê","thủy tinh","nhựa","cao su","vải","len","lụa","gấm","nhung","da","giấy","bìa","carton","xốp","mút","keo","băng dính","dây thun","dây thừng","dây điện","ổ cắm","công tắc","cầu dao","aptomat","biến áp","mô tơ","động cơ","máy bơm","máy nén","máy phát","quạt hút","quạt thông gió","máy lọc nước","máy nước nóng","bồn cầu","chậu rửa","vòi nước","sen tắm","bồn tắm","lavabo","gương soi","kệ","tủ giày","móc áo","phơi đồ","bàn chải","kem đánh răng","xà bông","dầu gội","sữa tắm","khăn tắm","khăn mặt","bàn là","cây lau nhà","cây chổi","cây gậy","cây búa","cây kéo","cây bút","cây thước","cây nến","cây quạt","cây đàn","cây sáo","cây kèn","cây trống"]

dia_diem = ["trường học","bệnh viện","nhà","công viên","siêu thị","chợ","rạp chiếu phim","nhà hàng","quán ăn","quán cà phê","sân bay","nhà ga","bến xe","bãi biển","trên núi","trong rừng","ngã tư","văn phòng","công ty","nhà máy","công trường","thư viện","nhà sách","phòng tập","hồ bơi","khách sạn","tiệm hớt tóc","ngân hàng","bưu điện","phòng ngủ","phòng khách","nhà bếp","sân vườn","ban công","tầng hầm","sân thượng","gara","nhà kho","nhà xe","bãi đỗ xe","trạm xăng","trạm xe buýt","bến tàu","bến phà","cảng biển","sân vận động","nhà thi đấu","cung văn hóa","nhà hát","bảo tàng","triển lãm","đền","chùa","nhà thờ","miếu","lăng","nghĩa trang","công viên nước","khu vui chơi","vườn thú","vườn bách thảo","khu bảo tồn","trại hè","trại giam","đồn công an","trụ sở","tòa án","quốc hội","phủ chủ tịch","đại sứ quán","lãnh sự quán","biên giới","cửa khẩu","hải quan","trạm thu phí","cầu","hầm","đèo","eo biển","vịnh","vũng","đầm","hồ","sông","suối","thác","ao","giếng","kênh","mương","rạch","bờ biển","bờ sông","bờ hồ","đảo","bán đảo","quần đảo","núi lửa","hang động","thung lũng","cao nguyên","đồng bằng","sa mạc","ốc đảo","thảo nguyên","rừng nhiệt đới","rừng nguyên sinh","rừng ngập mặn"]

mau_sac = ["đỏ","xanh","xanh lá","xanh dương","xanh trời","xanh biển","xanh ngọc","xanh rêu","xanh lá mạ","xanh lục","xanh lam","xanh chàm","vàng","vàng chanh","vàng cam","vàng nghệ","vàng tươi","vàng đất","tím","tím than","tím hoa cà","tím lavender","hồng","hồng nhạt","hồng đậm","hồng phấn","hồng sen","cam","cam đất","cam cháy","đen","đen tuyền","đen bóng","đen mờ","trắng","trắng sữa","trắng ngà","trắng tinh","trắng xám","xám","xám tro","xám bạc","xám khói","nâu","nâu đất","nâu gỗ","nâu chocolate","nâu cà phê","kem","kem sữa","bạc","đồng","đồng đỏ","đồng thau","chanh","chàm","ngọc","rêu","hổ phách","san hô","tràm","đỏ đô","đỏ tươi","đỏ thẫm","đỏ son","đỏ rượu vang","đỏ gạch","đỏ cam"]

trai_cay = ["táo","chuối","cam","dưa hấu","xoài","ổi","mận","đào","nho","dâu","dừa","dứa","khóm","đu đủ","sầu riêng","măng cụt","vải","nhãn","chôm chôm","mãng cầu","lựu","mắc ca","óc chó","hồng","sung","vú sữa","sapoche","bơ","thanh long","kiwi","cherry","dâu tây","việt quất","mâm xôi","phúc bồn tử","lý gai","me","táo tàu","táo mèo","táo gai","sung mỹ","đào tiên","chà là","ô liu","hạnh nhân","hạt dẻ","hạt điều","hạt bí","hạt hướng dương","hạt dưa"]

rau_cu = ["cải","cải ngọt","cải xanh","cải bó xôi","cải thìa","cải cúc","cải xoăn","rau muống","rau ngót","rau dền","rau mồng tơi","rau đay","rau rút","rau cần","rau ngò","rau mùi","rau húng","rau quế","rau tía tô","rau kinh giới","rau diếp cá","rau xà lách","rau bắp cải","bắp cải trắng","bắp cải tím","bông cải","súp lơ","cà rốt","củ cải","củ dền","su hào","khoai tây","khoai lang","khoai môn","khoai sọ","khoai mì","sắn","củ năng","củ sen","củ gừng","củ nghệ","củ tỏi","củ hành","hành lá","hành tím","hành tây","ớt","ớt chuông","cà chua","cà tím","cà pháo","đậu bắp","đậu cô ve","đậu hà lan","đậu que","đậu đũa","bí đỏ","bí xanh","bí đao","mướp","mướp đắng","khổ qua","dưa leo","dưa chuột","dưa gang","dưa hồng","giá đỗ","măng tây","măng tre","nấm rơm","nấm mèo","nấm hương","nấm kim châm","nấm đùi gà","nấm bào ngư","nấm đông cô","ngó sen","rau mầm","rau thơm","rau sống","rau luộc","rau xào","rau trộn"]

hoa = ["hồng","cúc","lan","huệ","loa kèn","ly","tuylip","thủy tiên","lay ơn","cẩm chướng","đồng tiền","sao","thược dược","trạng nguyên","mào gà","sen","súng","dâm bụt","phượng","bằng lăng","muồng","điệp","giấy","xuyến chi","bồ công anh","cỏ may","cỏ ba lá","hướng dương","cẩm tú cầu","tử đằng","anh đào","đào","mơ","mai","quỳnh","dạ lý hương","nhài","mộc","hoàng lan","ngọc lan","sứ","đại","lan hồ điệp","lan vũ nữ","lan hài","lan quế","hồng leo","hồng cổ","hồng bạch","hồng nhung","hồng vàng","hồng xanh"]

hanh_dong = ["ăn","uống","ngủ","chơi","học","làm","chạy","đi","hát","múa","nhảy","vẽ","viết","đọc","nghe","nói","xem","cười","khóc","suy nghĩ","tìm kiếm","lập trình","mua sắm","nấu ăn","dọn dẹp","tắm rửa","lái xe","đi bộ","leo núi","bơi lội","đạp xe","chạy bộ","tập yoga","tập gym","đá bóng","đánh cầu","chơi cờ","chơi game","xem phim","nghe nhạc","đọc sách","viết thư","gọi điện","nhắn tin","học bài","làm bài","thi cử","phỏng vấn","họp","thuyết trình","giảng bài","chữa bệnh","khám bệnh","bán hàng","mua hàng","trả tiền","tiết kiệm","đầu tư","vay mượn","cho vay","tặng quà","nhận quà","chụp ảnh","quay phim","vẽ tranh","điêu khắc","nấu cơm","rửa chén","lau nhà","giặt đồ","phơi đồ","ủi đồ","gấp đồ","đan lát","may vá","thêu thùa","đóng giày","sửa xe","sửa điện","sửa nước","xây nhà","đổ bê tông","trồng cây","tưới cây","cắt cỏ","hái quả","câu cá","săn bắn","chăn nuôi","gieo hạt","gặt lúa"]

tinh_cam = ["vui","buồn","mệt","đói","khát","tức giận","hạnh phúc","lo lắng","sợ hãi","bất ngờ","bình tĩnh","tự tin","thông minh","dũng cảm","tốt bụng","hiền lành","vui vẻ","nhiệt tình","chăm chỉ","trung thực","kiên nhẫn","sáng tạo","thấu hiểu","hào hứng","phấn khích","thư giãn","căng thẳng","hồi hộp","ngạc nhiên","xúc động","cảm động","biết ơn","hối hận","ghen tị","ghen tuông","ghen ghét","yêu thương","thương xót","đồng cảm","tôn trọng","khinh bỉ","coi thường","tự hào","khiêm tốn","kiêu ngạo","ích kỷ","vị tha","nhân hậu","độc ác","hung dữ","hiếu thảo","bất hiếu","trung thành","phản bội","thật thà","dối trá","ngây thơ","khờ khạo","lanh lợi","nhanh nhẹn","chậm chạp","lười biếng","siêng năng","cần cù","chịu khó","lạc quan","bi quan","yêu đời","chán đời","mệt mỏi","sảng khoái","khỏe khoắn","ốm yếu","đau đớn","sung sướng","khổ sở","vất vả","nhàn nhã","rảnh rỗi","bận rộn"]

nghe_nghiep = ["bác sĩ","y sĩ","y tá","giáo viên","học sinh","sinh viên","kỹ sư","lập trình viên","họa sĩ","ca sĩ","diễn viên","thợ may","thợ mộc","thợ điện","thợ hàn","thợ xây","đầu bếp","phi công","tiếp viên","cảnh sát","bộ đội","nông dân","ngư dân","lâm tặc","thợ săn","thợ lặn","thợ mỏ","thợ sơn","thợ nề","thợ đá","thợ bạc","thợ vàng","thợ gốm","thợ nhuộm","thợ dệt","thợ in","thợ chụp ảnh","thợ quay phim","thợ trang điểm","thợ làm tóc","thợ làm móng","nhân viên bán hàng","nhân viên thu ngân","nhân viên phục vụ","nhân viên giao hàng","tài xế taxi","tài xế xe bus","tài xế xe tải","trưởng phòng","giám đốc","chủ tịch","thư ký","kế toán","luật sư","thẩm phán","công tố viên","kiểm sát viên","công chứng viên","nhà báo","phóng viên","biên tập viên","nhà văn","nhà thơ","nhà nghiên cứu","giáo sư","tiến sĩ","thạc sĩ","nghiên cứu sinh","dược sĩ","nha sĩ","bác sĩ thú y","nhà tâm lý học","nhà xã hội học","nhà kinh tế","nhà ngoại giao","nhà chính trị","nhà quân sự","cảnh sát trưởng","đội trưởng","trung úy","thượng úy","đại úy","thiếu tá","trung tá","thượng tá","đại tá","tướng"]

bo_phan = ["đầu","tóc","trán","mắt","lông mày","lông mi","mũi","miệng","môi","răng","lưỡi","cằm","má","tai","cổ","vai","ngực","bụng","lưng","eo","hông","mông","đùi","đầu gối","bắp chân","cẳng chân","cổ chân","bàn chân","ngón chân","cánh tay","cùi chỏ","cổ tay","bàn tay","ngón tay","móng tay","da","thịt","xương","máu","tim","phổi","gan","thận","dạ dày","ruột","tụy","lá lách","túi mật","não","tủy","dây thần kinh","mạch máu","tĩnh mạch","động mạch","cơ","gân","sụn","khớp","răng nanh","răng cửa","răng hàm","răng khôn","lợi","vòm miệng","thực quản","khí quản","phế quản","ruột non","ruột già","trực tràng","bàng quang","niệu quản","tuyến giáp","tuyến thượng thận","tuyến yên","tuyến tụy","tuyến nước bọt","tuyến mồ hôi","tuyến sữa"]

thoi_tiet = ["nắng","mưa","gió","bão","lốc","sấm","sét","mây","mù","sương","tuyết","mưa đá","mưa phùn","mưa rào","mưa dông","mưa ngâu","mưa bão","nắng đẹp","nắng nóng","nắng gắt","nắng chói","âm u","u ám","râm mát","mát mẻ","se lạnh","lạnh giá","rét đậm","rét hại","nóng bức","oi bức","oi ả","hanh khô","ẩm ướt","ngột ngạt","trong lành","trong xanh","quang đãng","đẹp trời","xấu trời","thất thường","khắc nghiệt","dễ chịu","khó chịu"]

am_thanh = ["tiếng nói","tiếng cười","tiếng khóc","tiếng hát","tiếng đàn","tiếng sáo","tiếng trống","tiếng kèn","tiếng vĩ cầm","tiếng piano","tiếng guitar","tiếng sáo diều","tiếng chim hót","tiếng gà gáy","tiếng chó sủa","tiếng mèo kêu","tiếng vịt kêu","tiếng bò rống","tiếng hổ gầm","tiếng sói hú","tiếng voi rống","tiếng ngựa hí","tiếng dế mèn","tiếng ve sầu","tiếng ếch nhái","tiếng côn trùng","tiếng mưa rơi","tiếng gió thổi","tiếng sóng vỗ","tiếng thác đổ","tiếng suối chảy","tiếng sấm rền","tiếng sét đánh","tiếng nổ","tiếng súng","tiếng pháo","tiếng còi","tiếng chuông","tiếng trống trường","tiếng bước chân","tiếng gõ cửa","tiếng vỗ tay","tiếng huýt sáo","tiếng thì thầm","tiếng hò hét","tiếng la hét","tiếng gào thét"]

mon_an = ["phở","bún","miến","mì","hủ tiếu","bánh canh","bánh đa","bánh cuốn","bánh xèo","bánh khọt","bánh bèo","bánh bột lọc","bánh ướt","bánh chưng","bánh tét","bánh giò","bánh bao","bánh mì","bánh ngọt","bánh kem","bánh quy","bánh bông lan","bánh trung thu","bánh flan","bánh pudding","chè","chè đậu","chè ba màu","chè thái","chè khúc bạch","xôi","xôi gấc","xôi đậu","xôi mặn","cơm","cơm tấm","cơm rang","cơm chiên","cơm gà","cơm sườn","cơm bụi","cơm hến","cháo","cháo lòng","cháo gà","cháo cá","cháo vịt","cháo hến","cháo đậu","canh","canh chua","canh bí","canh rau","canh khổ qua","súp","súp gà","súp cua","salad","gỏi","gỏi cuốn","gỏi bò","gỏi gà","nem","nem chua","nem nướng","chả","chả giò","chả cá","chả lụa","chả trứng","thịt nướng","thịt kho","thịt xào","thịt luộc","thịt quay","thịt bò","thịt heo","thịt gà","thịt vịt","thịt dê","thịt cừu","cá chiên","cá hấp","cá kho","cá nướng","cá luộc","cá rán","tôm chiên","tôm hấp","tôm nướng","mực xào","mực chiên","mực nướng","lẩu","lẩu thái","lẩu nấm","lẩu bò","lẩu hải sản"]

the_thao = ["bóng đá","bóng rổ","bóng chuyền","bóng bàn","bóng ném","bóng nước","bóng chày","bóng bầu dục","cầu lông","quần vợt","bơi lội","điền kinh","chạy marathon","chạy việt dã","đua xe","đua ngựa","đua thuyền","đua xe đạp","thể dục dụng cụ","gym","yoga","aerobic","karate","judo","taekwondo","vovinam","võ cổ truyền","boxing","muay thái","vật","cử tạ","bắn cung","bắn súng","cưỡi ngựa","leo núi","trượt tuyết","trượt băng","lướt sóng","lướt ván","nhảy dù","nhảy cầu","đánh golf","đánh cờ","đánh bài","đấu kiếm","đá cầu","nhảy dây","kéo co","nhảy xa","nhảy cao","đẩy gậy","ném đĩa","ném lao","cầu mây","pickleball","futsal"]

phuong_tien = ["xe đạp","xe máy","xe ôm","xe taxi","xe buýt","xe tải","xe container","xe khách","xe du lịch","xe cứu thương","xe cứu hỏa","xe cảnh sát","xe tang","xe ba gác","xe lam","xe xích lô","xe lôi","xe kéo","xe bò","xe ngựa","tàu hỏa","tàu điện","tàu điện ngầm","tàu cao tốc","tàu thủy","tàu du lịch","tàu ngầm","tàu sân bay","tàu chiến","tàu cá","tàu vũ trụ","phi thuyền","máy bay","máy bay phản lực","máy bay trực thăng","máy bay ném bom","máy bay tiêm kích","tên lửa","vệ tinh","trạm không gian","khinh khí cầu","dù lượn","mô tô","xế hộp","xế độ","xế cổ","siêu xe","xe thể thao","xe limousine"]

vat_lieu = ["gỗ","gỗ tự nhiên","gỗ công nghiệp","sắt","thép","gang","nhôm","đồng","đồng đỏ","đồng thau","chì","kẽm","thiếc","vàng","bạc","bạch kim","kim cương","đá quý","ruby","sapphire","emerald","ngọc trai","san hô","hổ phách","pha lê","thủy tinh","nhựa","nhựa PVC","nhựa PE","nhựa ABS","cao su","cao su non","vải","vải cotton","vải lụa","vải len","vải dạ","vải nhung","vải gấm","vải kaki","vải jean","vải thô","vải voan","da","da bò","da cá sấu","da trăn","da cừu","da nhân tạo","giấy","bìa","carton","giấy báo","giấy vệ sinh","giấy ăn","xốp","mút","mút xốp","keo","keo dán","keo nến","băng dính","băng keo","gốm","sứ","đất sét","đất nung","xi măng","bê tông","gạch","ngói","đá","đá hoa cương","đá cẩm thạch","đá granite","đá marble","thạch cao","amiăng","carbon","sợi thủy tinh","sợi carbon","sợi tổng hợp","kim loại","hợp kim","inox","titan"]

hinh_dang = ["tròn","vuông","chữ nhật","tam giác","lục giác","bát giác","ngũ giác","thất giác","bầu dục","oval","elip","parabol","hyperbol","xoắn ốc","lượn sóng","gợn sóng","hình tim","hình sao","hình trăng","hình hoa","hình lá","hình cầu","hình trụ","hình nón","hình chóp","hình hộp","hình lập phương","hình thoi","hình bình hành","hình thang","hình quạt","hình vành khuyên","hình xuyến","hình xoắn","hình phễu","hình giọt nước","hình yên ngựa","hình móng ngựa"]

kich_thuoc = ["khổng lồ","to lớn","vĩ đại","đồ sộ","hoành tráng","bự","to","lớn","vừa","trung bình","nhỏ","bé","nhỏ xíu","tí hon","tí xíu","li ti","nhỏ nhắn","thon gọn","mảnh khảnh","thon thả","mập mạp","béo tốt","tròn trịa","mũm mĩm","gầy guộc","ốm nhom","cao","cao lớn","cao ráo","lùn","thấp","thấp bé","dài","ngắn","rộng","hẹp","dày","mỏng","nặng","nhẹ","sâu","nông","xa","gần"]

gia_vi = ["muối","đường","tiêu","ớt","tỏi","hành","gừng","nghệ","sả","riềng","quế","hồi","đinh hương","thảo quả","hạt mùi","hạt thì là","hạt cần tây","hạt nhục đậu khấu","bột ngọt","bột nêm","hạt nêm","nước mắm","nước tương","xì dầu","dầu hào","tương ớt","tương cà","mayonnaise","mù tạt","wasabi","giấm","giấm táo","giấm gạo","rượu","rượu vang","rượu trắng","bia","cà phê","trà","mật ong","siro","chanh","quất","tắc","me","tamarind","ớt bột","ớt tươi","ớt khô"]

dung_cu = ["búa","đục","cưa","khoan","máy khoan","máy cắt","máy mài","máy hàn","máy tiện","máy phay","máy bào","máy đục","máy đánh bóng","máy nén khí","máy bơm nước","máy phát điện","máy hút bụi","máy thổi lá","máy cắt cỏ","máy xới đất","máy trộn bê tông","máy đầm","máy xúc","máy ủi","máy cẩu","xe rùa","xẻng","cuốc","cào","liềm","hái","rựa","dao phay","dao thái","dao gọt","dao rọc giấy","dao cạo","dao lam","bàn chải sắt","giũa","dũa","đe","kìm","cờ lê","mỏ lết","tua vít","vít","ốc","bu lông","đai ốc","vòng đệm","long đền","chốt","chìa vặn","cưa tay","cưa máy","cưa lọng","cưa xích","đinh","đinh vít","ghim","kẹp","kẹp giấy","kẹp gỗ","băng đô"]

thiet_bi = ["máy tính bàn","laptop","máy tính bảng","smartphone","smartwatch","smart TV","tivi","máy chiếu","loa bluetooth","loa kéo","tai nghe","tai nghe chụp tai","tai nghe nhét tai","tai nghe bluetooth","micro","ampli","receiver","đầu đĩa","đầu karaoke","amly karaoke","cục đẩy công suất","máy ảnh DSLR","máy ảnh mirrorless","máy ảnh compact","máy quay phim","flycam","webcam","máy in","máy scan","máy photocopy","máy fax","máy hủy tài liệu","máy đếm tiền","máy chấm công","máy tính tiền","máy in hóa đơn","máy pos","máy quét mã vạch","máy in mã vạch","máy đọc thẻ","máy rút tiền ATM","máy đổi tiền","máy bán nước tự động","máy bán hàng tự động","máy massage","máy đo huyết áp","máy đo đường huyết","máy đo nhiệt độ","máy đo nhịp tim","máy đo nồng độ oxy","máy trợ thính","máy khử trùng","máy tạo ẩm","máy hút ẩm","máy lọc không khí","máy sưởi","máy nước nóng","máy nước lạnh"]

do_uong = ["nước lọc","nước khoáng","nước tinh khiết","nước suối","nước ngọt","nước có ga","nước cam","nước chanh","nước dừa","nước mía","nước ép táo","nước ép cà rốt","nước ép cần tây","nước ép cà chua","nước ép thơm","nước ép ổi","nước ép nho","nước ép lựu","sinh tố bơ","sinh tố xoài","sinh tố chuối","sinh tố dâu","sinh tố mãng cầu","sữa tươi","sữa chua","sữa đặc","sữa bột","sữa đậu nành","sữa gạo","sữa hạt","sữa yến mạch","sữa hạnh nhân","sữa óc chó","cà phê đen","cà phê sữa","cà phê muối","cà phê trứng","bạc xỉu","trà đá","trà nóng","trà xanh","trà đen","trà ô long","trà sen","trà hoa cúc","trà hoa hồng","trà gừng","trà sữa","trà sữa trân châu","trà sữa matcha","trà sữa thái","trà trái cây","trà đào","trà vải","trà chanh","trà tắc","bia","bia hơi","bia lon","bia chai","rượu vang đỏ","rượu vang trắng","rượu sâm banh","rượu whisky","rượu vodka","rượu rum","rượu tequila","rượu mơ","rượu nếp","rượu cần"]

thuc_vat = ["lúa","ngô","khoai","sắn","đậu","mè","vừng","lạc","hướng dương","cà phê","ca cao","chè","hồ tiêu","điều","cao su","dừa","cau","trầu","tre","trúc","nứa","bương","vầu","hóp","lồ ô","dừa nước","bần","đước","mắm","sú","vẹt","dà","cóc","gừa","phi lao","keo","bạch đàn","thông","tùng","bách","xà cừ","lim","sến","gõ đỏ","gụ","cẩm lai","trắc","sưa","giáng hương","hoàng đàn","pơ mu","sa mộc","thông đỏ","thông năm lá","tuế","vạn tuế","dương xỉ","rêu","địa y","tảo","rong","rong biển","rong mơ","rong nho","rong câu","bèo","bèo tấm","bèo lục bình","sen","súng","rau dừa nước","cỏ","cỏ voi","cỏ lông chông","cỏ gà","cỏ may","cỏ chỉ"]

nha_cua = ["cửa chính","cửa phụ","cửa sổ","cửa sổ trời","cửa kính","cửa gỗ","cửa sắt","cửa cuốn","cửa xếp","cửa tự động","cửa xoay","cửa lùa","cửa nhôm","cửa nhựa","cửa chống cháy","cửa chống trộm","cửa cách âm","cửa cách nhiệt","cửa vòm","cửa hai cánh","cửa bốn cánh","lan can","ban công","sân thượng","sân trước","sân sau","hiên nhà","mái hiên","mái bằng","mái tôn","mái ngói","mái lá","mái thái","mái nhật","tường","tường gạch","tường bê tông","tường đá","tường gỗ","tường kính","tường ngăn","tường chịu lực","tường cách âm","tường cách nhiệt","tường trang trí","tường ốp gỗ","tường ốp đá","tường ốp gạch","tường sơn nước","tường giấy dán","cầu thang","cầu thang xoắn","cầu thang thẳng","cầu thang chữ L","cầu thang chữ U","cầu thang bộ","cầu thang máy","cầu thang gỗ","cầu thang sắt","cầu thang inox","cầu thang bê tông","cầu thang đá","cầu thang kính"]

con_vat_bien = ["cá heo","cá voi xanh","cá voi sát thủ","cá nhà táng","cá mập trắng","cá mập hổ","cá mập đầu búa","cá đuối điện","cá đuối ó","cá đuối bồng","cá ngừ đại dương","cá kiếm","cá buồm","cá cờ","cá thu ngừ","cá trích","cá cơm","cá mòi","cá nục","cá hồng","cá mú","cá chẽm","cá song","cá bớp","cá giò","cá đé","cá đù","cá lượng","cá hố","cá lịch","cá chình","cá lươn","cá trạch","cá kèo","cá bống","cá thòi lòi","cá rô đồng","cá rô phi","cá diêu hồng","cá điêu hồng","cá chim trắng","cá chim đen","cá ba sa","cá tra","cá basa","cá trắm","cá mè","cá chép","cá vàng","cá rồng","cá la hán","cá betta","cá bảy màu","cá đĩa","cá tỳ bà","cá chuột","cá mún","cá hồi","cá tầm","cá hồi vân","cá hồi đỏ","cá trê","cá trê vàng","cá trê trắng","cá nheo","cá ngát","cá úc","cá chỉ vàng","cá phèn","cá liệt","cá móm","cá đối","cá khoai","cá bạc má","cá miễn sành"]

cach_dien_dat = ["rất","quá","lắm","cực kỳ","vô cùng","hết sức","siêu","thật","thiệt","cực","khá","hơi","hơi hơi","tương đối","hơi bị","khá là","có vẻ","dường như","hình như","chắc là","chắc hẳn","đúng là","quả nhiên","thực sự","thật sự","đích thực","chính hiệu","hàng thật","hàng xịn","hàng hiệu","cao cấp","sang trọng","quý phái","bình dân","dân dã","đơn giản","mộc mạc","giản dị","cầu kỳ","tinh tế","tinh xảo","khéo léo","tài tình","điêu luyện","siêu phàm","tuyệt vời","tuyệt hảo","hoàn hảo","hoàn mỹ","vô địch","bất bại","bất hủ","vĩnh cửu","trường tồn"]

tinh_tu = ["đẹp","xấu","to","nhỏ","bé","lớn","khổng lồ","nhỏ xíu","mới","cũ","nhanh","chậm","khỏe","yếu","cao","thấp","dài","ngắn","rộng","hẹp","nặng","nhẹ","nóng","lạnh","ấm","mát","mềm","cứng","sắc","cùn","tròn","vuông","đắt","rẻ","đẹp đẽ","xinh xắn","dễ thương","đáng yêu","đáng mến","thú vị","nhàm chán","hấp dẫn","lôi cuốn","mê hoặc","quyến rũ","thanh lịch","sang trọng","quý phái","bình dị","mộc mạc","giản dị","tinh tế","thô kệch","mịn màng","sần sùi","bóng loáng","mờ ảo","sáng chói","tối om","âm u","u ám","quang đãng","trong veo","đục ngầu","tinh khiết","thuần khiết","nguyên chất","hỗn tạp","đa dạng","phong phú","nghèo nàn","sung túc","đầy đủ","thiếu thốn","dư dả","chan hòa","hài hòa","cân đối","lệch lạc","ổn định","bất ổn","yên tĩnh","ồn ào","náo nhiệt","vắng vẻ","đông đúc","thưa thớt","san sát","rải rác","lác đác","tấp nập","nhộn nhịp"]


do_choi = ["búp bê","gấu bông","xe đồ chơi","máy bay đồ chơi","tàu hỏa đồ chơi","robot đồ chơi","siêu nhân","bộ xếp hình","lego","rubik","yo-yo","con quay","bắn bi","bi","bóng bay","bóng nhựa","bóng da","diều","diều giấy","chong chóng","lồng đèn","đèn ông sao","trống cơm","trống lắc","kèn đồ chơi","sáo đồ chơi","xylophone","đàn đồ chơi","bộ đồ bếp","bộ đồ bác sĩ","bộ đồ thợ xây","bộ đồ câu cá","câu cá nam châm","bộ đồ nấu ăn","bộ đồ bán hàng","tô màu","bút màu","sáp màu","màu nước","đất nặn","slime","bong bóng xà phòng","thú nhún","nhà banh","cầu trượt","xích đu","bập bênh","đu quay","nhà bóng","hồ bóng","xe scooter","xe trượt","pa-tanh","giày trượt","ván trượt","con lăn","cờ cá ngựa","cờ tỷ phú","cờ vua","cờ tướng","cờ vây","cờ caro","cờ domino","xếp hình","xếp giấy","origami","đồ hàng mã","tò he","đèn kéo quân","mặt nạ","mũ giấy","vương miện","gậy phép","đũa thần","thảm bay","chổi thần"]

nhac_cu = ["đàn piano","đàn guitar","đàn guitar điện","đàn guitar bass","đàn violin","đàn cello","đàn viola","đàn contrabass","đàn tranh","đàn bầu","đàn nguyệt","đàn tỳ bà","đàn tam","đàn nhị","đàn kìm","đàn đá","đàn t'rưng","đàn klông pút","đàn đáy","đàn sến","đàn gáo","sáo trúc","sáo ngang","sáo dọc","sáo bầu","tiêu","kèn harmonica","kèn trumpet","kèn saxophone","kèn clarinet","kèn oboe","kèn bassoon","kèn trombone","kèn tuba","kèn cor","trống cái","trống con","trống lắc","trống cơm","trống jazz","trống điện tử","trống định âm","trống djembe","trống bongo","trống conga","trống taiko","trống trận","trống hội","phách","song loan","mõ","chuông","lục lạc","thanh la","tam âm","cồng","chiêng","đàn organ","đàn synth","đàn accordion","kèn túi","đàn harp","đàn ukulele","đàn banjo","đàn mandolin","đàn sitar"]

vu_khi = ["gươm","kiếm","dao găm","đoản đao","trường kiếm","đại đao","cung","nỏ","tên","giáo","thương","mác","kích","rìu","búa chiến","chuỳ","côn","gậy","roi","dùi cui","súng lục","súng trường","súng máy","súng ngắn","súng bắn tỉa","súng shotgun","súng tiểu liên","súng phóng lựu","súng cối","súng đại bác","súng rocket","súng phun lửa","mìn","lựu đạn","bom","bom xăng","thuốc nổ","ngư lôi","tên lửa đạn đạo","tên lửa hành trình","tên lửa chống tăng","tên lửa phòng không","máy bay chiến đấu","máy bay ném bom","máy bay do thám","xe tăng","xe bọc thép","thiết giáp","tàu chiến","tàu sân bay","tàu ngầm quân sự","khiên","giáp","mũ giáp","giáp ngực","bao tay sắt","ống chân","yên ngựa","dây cương","khoá","xích","roi da","phi tiêu","móc câu","dùi","đục","dao rựa","dao phóng","dao bầu","dao quắm","dao găm","chùy sắt","chùy gai","dùi cui điện"]

do_trang_suc = ["nhẫn vàng","nhẫn bạc","nhẫn kim cương","nhẫn cưới","nhẫn đính hôn","bông tai vàng","bông tai bạc","bông tai ngọc trai","bông tai kim cương","dây chuyền vàng","dây chuyền bạc","dây chuyền ngọc","vòng cổ","vòng tay vàng","vòng tay bạc","vòng tay ngọc","lắc tay","lắc chân","kiềng vàng","kiềng bạc","xuyến bạc","trâm cài tóc","kẹp tóc","bờm tóc","vương miện","vòng hoa","hoa tai","khuyên tai","khuyên mũi","khuyên rốn","khuyên lưỡi","nhẫn ngón chân","chuỗi hạt","mala","tràng hạt","thánh giá","mặt dây chuyền","bùa hộ mệnh","bùa may mắn","vòng phong thủy","vòng đá","vòng gỗ","vòng trầm hương","vòng tỳ hưu","vòng thạch anh","vòng mã não","vòng ngọc bích","vòng phỉ thúy","vòng đá mắt hổ","vòng đá thạch anh tím","nhẫn cẩm thạch","nhẫn phật bà","mặt ngọc","mặt cẩm thạch","mặt đá quý"]

benh_tat = ["cảm cúm","cảm lạnh","sốt","sốt xuất huyết","sốt rét","sốt phát ban","ho","ho khan","ho có đờm","viêm họng","viêm amidan","viêm phế quản","viêm phổi","viêm xoang","viêm mũi dị ứng","hen suyễn","lao phổi","tràn dịch màng phổi","đau đầu","đau nửa đầu","chóng mặt","hoa mắt","ù tai","mất ngủ","suy nhược","trầm cảm","lo âu","rối loạn lo âu","tự kỷ","tăng động","đau dạ dày","viêm dạ dày","loét dạ dày","trào ngược dạ dày","đau ruột thừa","viêm ruột thừa","tiêu chảy","táo bón","kiết lỵ","tả","thương hàn","đau gan","viêm gan A","viêm gan B","viêm gan C","xơ gan","ung thư gan","sỏi thận","sỏi mật","suy thận","viêm thận","viêm bàng quang","tiểu đường","cao huyết áp","huyết áp thấp","xơ vữa động mạch","nhồi máu cơ tim","đột quỵ","tai biến","béo phì","suy dinh dưỡng","thiếu máu","thiếu canxi","thiếu vitamin","còi xương","loãng xương","gout","viêm khớp","thoái hóa khớp","thoát vị đĩa đệm","đau lưng","đau cổ vai gáy","bong gân","gãy xương","nứt xương","trật khớp","bỏng","bỏng nước sôi","bỏng lửa","bỏng hóa chất","dị ứng","mề đay","nổi mẩn","nổi mụn","trứng cá","vảy nến","chàm","lang ben","nấm da","nấm móng","ghẻ","ve chó","chấy","rận","mụn cóc","mụn rộp","zona","thủy đậu","quai bị","sởi","rubella","đậu mùa","bại liệt","uốn ván","dại","HIV","AIDS"]

trieu_chung = ["sốt cao","sốt nhẹ","ớn lạnh","rùng mình","vã mồ hôi","đổ mồ hôi đêm","đau họng","đau họng rát","khó nuốt","nghẹn","nôn","buồn nôn","nôn mửa","chóng mặt","xây xẩm","hoa mắt","nhức đầu","đau nhức toàn thân","mỏi cơ","mỏi khớp","đau khớp","sưng khớp","cứng khớp","tê tay","tê chân","tê bì","yếu cơ","chuột rút","run rẩy","co giật","động kinh","mất ý thức","ngất","hôn mê","khó thở","thở gấp","thở khò khè","ngạt mũi","chảy nước mũi","hắt hơi","ngứa mũi","ngứa mắt","chảy nước mắt","đỏ mắt","sưng mắt","mờ mắt","nhìn đôi","giảm thị lực","mất thị lực","ù tai","giảm thính lực","điếc","chán ăn","ăn không ngon","ăn không tiêu","đầy bụng","chướng bụng","ợ chua","ợ nóng","khát nước","khô miệng","khô môi","nứt môi","chảy máu cam","chảy máu chân răng","bầm tím","xuất huyết","phù nề","sưng phù","vàng da","vàng mắt","tiểu buốt","tiểu rắt","tiểu ra máu","tiểu đêm","tiểu không kiểm soát"]

hành_tinh_sao = ["sao Thủy","sao Kim","Trái Đất","sao Hỏa","sao Mộc","sao Thổ","sao Thiên Vương","sao Hải Vương","sao Diêm Vương","Mặt Trời","Mặt Trăng","sao Bắc Cực","sao Bắc Đẩu","sao Hôm","sao Mai","sao Chổi","sao Băng","sao Đổi Ngôi","sao Kim Tinh","sao Hỏa Tinh","sao Mộc Tinh","sao Thổ Tinh","sao Thủy Tinh","sao Hải Tinh","sao Thiên Tinh","sao Diêm Tinh","Ngân Hà","Dải Ngân Hà","Thiên Hà","hố đen","lỗ đen","tinh vân","thiên thạch","vẫn thạch","nhật thực","nguyệt thực","cực quang","tia vũ trụ","vụ nổ Big Bang","vũ trụ","thiên hà Andromeda","chòm sao Bạch Dương","chòm sao Kim Ngưu","chòm sao Song Tử","chòm sao Cự Giải","chòm sao Sư Tử","chòm sao Xử Nữ","chòm sao Thiên Bình","chòm sao Bọ Cạp","chòm sao Nhân Mã","chòm sao Ma Kết","chòm sao Bảo Bình","chòm sao Song Ngư"]

nguyen_to = ["Hydro","Heli","Liti","Beri","Bo","Cacbon","Nitơ","Oxy","Flo","Neon","Natri","Magie","Nhôm","Silic","Photpho","Lưu huỳnh","Clo","Argon","Kali","Canxi","Sắt","Coban","Niken","Đồng","Kẽm","Bạc","Thiếc","Vàng","Thủy ngân","Chì","Platin","Uranium","Radium","Titan","Crom","Mangan","Bo","Iot","Brom","Selen","Asen","Bari","Berili","Liti","Rubidi","Xesi","Franxi","Stronti","Ytri","Zicorni","Niobi","Molypden","Rutheni","Rhodi","Paladi","Cadimi","Indi","Antimon","Telu","Xenon","Krypton","Heli","Neon","Argon","Radon"]

quoc_gia = ["Việt Nam","Trung Quốc","Nhật Bản","Hàn Quốc","Triều Tiên","Thái Lan","Lào","Campuchia","Myanmar","Malaysia","Singapore","Indonesia","Philippines","Brunei","Đông Timor","Ấn Độ","Pakistan","Bangladesh","Sri Lanka","Nepal","Bhutan","Maldives","Afghanistan","Iran","Iraq","Ả Rập Xê Út","UAE","Qatar","Kuwait","Oman","Yemen","Jordan","Lebanon","Syria","Israel","Thổ Nhĩ Kỳ","Ai Cập","Libya","Tunisia","Algeria","Maroc","Sudan","Ethiopia","Kenya","Tanzania","Uganda","Nigeria","Ghana","Senegal","Nam Phi","Zimbabwe","Zambia","Mozambique","Angola","Nga","Ukraina","Belarus","Ba Lan","Đức","Pháp","Anh","Ireland","Hà Lan","Bỉ","Luxembourg","Thụy Sĩ","Áo","Ý","Tây Ban Nha","Bồ Đào Nha","Hy Lạp","Thụy Điển","Na Uy","Đan Mạch","Phần Lan","Iceland","Estonia","Latvia","Litva","Séc","Slovakia","Hungary","Romania","Bulgaria","Serbia","Croatia","Slovenia","Bosnia","Montenegro","Albania","Macedonia","Hoa Kỳ","Canada","Mexico","Brazil","Argentina","Chile","Peru","Colombia","Venezuela","Ecuador","Bolivia","Paraguay","Uruguay","Cuba","Jamaica","Haiti","Costa Rica","Panama","Guatemala","Honduras","Úc","New Zealand","Fiji","Papua New Guinea"]

tinh_thanh = ["Hà Nội","Hải Phòng","Quảng Ninh","Hải Dương","Hưng Yên","Thái Bình","Nam Định","Ninh Bình","Hà Nam","Bắc Ninh","Bắc Giang","Vĩnh Phúc","Thái Nguyên","Phú Thọ","Tuyên Quang","Yên Bái","Lào Cai","Hà Giang","Cao Bằng","Bắc Kạn","Lạng Sơn","Điện Biên","Lai Châu","Sơn La","Hòa Bình","Thanh Hóa","Nghệ An","Hà Tĩnh","Quảng Bình","Quảng Trị","Thừa Thiên Huế","Đà Nẵng","Quảng Nam","Quảng Ngãi","Bình Định","Phú Yên","Khánh Hòa","Ninh Thuận","Bình Thuận","Kon Tum","Gia Lai","Đắk Lắk","Đắk Nông","Lâm Đồng","Bình Phước","Tây Ninh","Bình Dương","Đồng Nai","Bà Rịa - Vũng Tàu","TP Hồ Chí Minh","Long An","Tiền Giang","Bến Tre","Trà Vinh","Vĩnh Long","Đồng Tháp","An Giang","Kiên Giang","Cần Thơ","Hậu Giang","Sóc Trăng","Bạc Liêu","Cà Mau","Sài Gòn","Hội An","Huế","Nha Trang","Đà Lạt","Vũng Tàu","Phan Thiết","Quy Nhơn","Buôn Ma Thuột","Pleiku","Rạch Giá","Mỹ Tho","Cao Lãnh","Vĩnh Long"]

le_hoi = ["Tết Nguyên Đán","Tết Nguyên Tiêu","Tết Hàn Thực","Tết Đoan Ngọ","Tết Trung Thu","Tết Trùng Cửu","Tết Thanh Minh","Lễ Vu Lan","Lễ Phật Đản","Lễ Giáng Sinh","Lễ Phục Sinh","Lễ Halloween","Lễ Tạ Ơn","Lễ Tình Nhân","Quốc tế Phụ nữ","Quốc tế Thiếu nhi","Quốc tế Lao động","Quốc khánh","Ngày Nhà giáo","Ngày Thầy thuốc","Ngày Phụ nữ Việt Nam","Ngày Gia đình Việt Nam","Ngày Thương binh Liệt sĩ","Ngày thành lập Đảng","Ngày thành lập Quân đội","Ngày thành lập Đoàn","Lễ hội Đền Hùng","Lễ hội Chùa Hương","Lễ hội Yên Tử","Lễ hội Gióng","Lễ hội Côn Sơn","Lễ hội Lim","Lễ hội Đống Đa","Hội An","Lễ hội hoa Đà Lạt","Lễ hội pháo hoa Đà Nẵng","Lễ hội áo dài","Lễ hội cà phê","Lễ hội trái cây","Lễ hội đua thuyền","Lễ hội đua voi","Lễ hội chọi trâu","Lễ hội chọi gà","Lễ hội đấu vật","Lễ hội ném còn","Lễ hội tung còn","Lễ hội múa lân","Lễ hội múa rồng","Lễ hội đèn lồng"]

tro_choi_dan_gian = ["nhảy dây","nhảy lò cò","nhảy sạp","nhảy bao bố","nhảy ngựa","đá cầu","đá cầu lông","đá gà","đá dế","đấu vật","kéo co","bịt mắt bắt dê","mèo đuổi chuột","rồng rắn lên mây","chi chi chành chành","nu na nu nống","lộn cầu vồng","tập tầm vông","cờ gánh","cờ caro","cờ vua","cờ tướng","cờ tỷ phú","bầu cua","xóc đĩa","lô tô","đánh bi","bắn bi","đánh đáo","đánh quay","đánh khăng","đánh phết","đánh chuyền","đánh chắt","đánh đũa","ném vòng","ném lon","ném còn","bắn ná","bắn súng nước","bong bóng","thả diều","chơi chuyền","chơi ô ăn quan","chơi cờ cá ngựa","chơi tổ tôm","chơi tam cúc","chơi tú lơ khơ","chơi xì dách","chơi tiến lên","chơi phỏm","chơi mậu binh","chơi ba cây","chơi liêng","chơi xì tố","chơi domino","chơi cờ domino"]

do_an_vat = ["bánh tráng","bánh tráng trộn","bánh tráng nướng","bánh tráng cuốn","bánh đa","bánh đa cua","bánh phồng","bánh phồng tôm","bánh xốp","bánh quế","bánh quy","bánh cracker","bánh snack","bánh khoai","bánh chuối","bánh cam","bánh rán","bánh tiêu","bánh bò","bánh da lợn","bánh đúc","bánh tai","bánh gai","bánh ít","bánh nếp","bánh tẻ","bánh gio","bánh đậu xanh","bánh pía","bánh trung thu","bánh in","bánh tổ","bánh thuẫn","kẹo","kẹo dẻo","kẹo cứng","kẹo mút","kẹo bông","kẹo socola","kẹo cao su","kẹo dừa","kẹo mè xửng","kẹo lạc","kẹo cu đơ","kẹo chanh","kẹo gừng","kẹo bạc hà","kẹo me","kẹo dâu","hạt dưa","hạt bí","hạt hướng dương","hạt điều","hạt macca","hạt óc chó","hạt hạnh nhân","hạt dẻ cười","hạt dẻ","hạt sen sấy","đậu phộng rang","đậu nành rang","khô gà","khô bò","khô mực","khô cá","cá viên chiên","bò viên","xúc xích","xiên que","há cảo","bánh bao chiên","phô mai que","khoai lang kén","khoai tây chiên","bắp rang bơ","bắp xào","bò bía","gỏi cuốn","bánh mì que","bánh mì chảo"]

linh_kien_may = ["CPU","GPU","RAM","ROM","SSD","HDD","ổ cứng","ổ cứng thể rắn","bo mạch chủ","mainboard","card đồ họa","card âm thanh","card mạng","nguồn máy tính","PSU","vỏ case","tản nhiệt","quạt tản nhiệt","tản nhiệt nước","keo tản nhiệt","bộ vi xử lý","vi xử lý","chip xử lý","chip nhớ","chip đồ họa","bộ nhớ trong","bộ nhớ ngoài","thanh RAM","thanh SSD","thanh HDD","ổ USB","thẻ nhớ SD","thẻ microSD","thẻ CF","thẻ nhớ Sony","đầu đọc thẻ","cáp USB","cáp HDMI","cáp VGA","cáp DVI","cáp DisplayPort","cáp mạng","dây mạng","cổng USB","cổng HDMI","cổng Type-C","cổng Thunderbolt","cổng lightning","bàn phím","chuột","chuột không dây","bàn phím cơ","bàn phím quang","tai nghe gaming","ghế gaming","màn hình","màn hình cong","màn hình 4K","màn hình 144Hz","webcam","micro thu âm","giá đỡ laptop","đế tản nhiệt","đế tản nhiệt laptop"]

ung_dung_web = ["Facebook","YouTube","TikTok","Instagram","Twitter","X","Snapchat","Telegram","WhatsApp","Messenger","Zalo","Viber","Line","WeChat","Discord","Reddit","Pinterest","LinkedIn","Tumblr","Flickr","Google","Bing","Yahoo","DuckDuckGo","Baidu","Yandex","Gmail","Outlook","Yahoo Mail","Google Drive","Dropbox","OneDrive","iCloud","Google Docs","Google Sheets","Google Slides","Microsoft Word","Microsoft Excel","Microsoft PowerPoint","Notion","Trello","Slack","Zoom","Google Meet","Microsoft Teams","Skype","Shopee","Lazada","Tiki","Sendo","Amazon","eBay","AliExpress","Taobao","Grab","Gojek","Be","Xanh SM","Uber","Airbnb","Booking","Agoda","Traveloka","Netflix","Disney+","HBO Max","Amazon Prime","Apple TV+","Spotify","Apple Music","YouTube Music","SoundCloud","Zing MP3","Nhaccuatui","Steam","Epic Games","GOG","Origin","PlayStation Store","Xbox Store","Nintendo eShop","Google Play","App Store","CH Play"]

game = ["Liên Quân","Liên Minh Huyền Thoại","LMHT Tốc Chiến","PUBG","PUBG Mobile","Free Fire","Call of Duty","Call of Duty Mobile","Genshin Impact","Honkai Star Rail","Honkai Impact","Minecraft","Roblox","Among Us","Fortnite","Apex Legends","Valorant","CS:GO","CS2","Dota 2","Dota Underlords","Overwatch","Overwatch 2","Diablo","Diablo Immortal","World of Warcraft","Starcraft","Warcraft","Age of Empires","Command & Conquer","Red Alert","Clash of Clans","Clash Royale","Brawl Stars","Hay Day","Boom Beach","Candy Crush","Angry Birds","Plants vs Zombies","Temple Run","Subway Surfers","Flappy Bird","Pokemon Go","Pokemon","Mario","Super Mario","Sonic","Zelda","Final Fantasy","Resident Evil","Silent Hill","GTA","GTA V","Red Dead Redemption","Assassin's Creed","Far Cry","Battlefield","FIFA","PES","eFootball","NBA 2K","Need for Speed","Forza","Gran Turismo","Mortal Kombat","Street Fighter","Tekken","The King of Fighters","Blazblue"]

bo_phim = ["Avengers","Iron Man","Captain America","Thor","Hulk","Spider-Man","Black Panther","Doctor Strange","Ant-Man","Guardians of the Galaxy","Captain Marvel","Black Widow","Shang-Chi","Eternals","Justice League","Batman","Superman","Wonder Woman","Aquaman","Flash","Cyborg","Green Lantern","Shazam","Joker","Harry Potter","Fantastic Beasts","Lord of the Rings","The Hobbit","Hobbit","Star Wars","Star Trek","Matrix","Terminator","Alien","Predator","Jurassic Park","Jurassic World","Transformers","Fast and Furious","Mission Impossible","James Bond","Indiana Jones","Pirates of the Caribbean","Titanic","Avatar","Inception","Interstellar","The Dark Knight","The Godfather","The Shawshank Redemption","Forrest Gump","Gladiator","Braveheart","Troy","300","The Avengers","Spider-Man No Way Home","Top Gun","John Wick","Kung Fu Panda","How to Train Your Dragon","Frozen","Moana","Coco","Toy Story","Finding Nemo","The Lion King","Aladdin","Beauty and the Beast","Tangled","Snow White","Cinderella","Mulan","Encanto","Raya and the Last Dragon"]

ca_si = ["Sơn Tùng M-TP","Hồ Ngọc Hà","Mỹ Tâm","Đàm Vĩnh Hưng","Lệ Quyên","Trấn Thành","Noo Phước Thịnh","Bảo Anh","Erik","Soobin Hoàng Sơn","Bích Phương","Hương Tràm","Hoàng Thùy Linh","Đông Nhi","Khởi My","Minh Hằng","Tóc Tiên","Trúc Nhân","Bùi Anh Tuấn","Uyên Linh","Văn Mai Hương","Thanh Bùi","Quang Vinh","Đan Trường","Nam Cường","Hồ Quang Hiếu","Duy Mạnh","Lâm Chấn Huy","Châu Khải Phong","Khắc Việt","Lê Bảo Bình","Vũ Cát Tường","Tiên Tiên","Thùy Chi","Hà Anh Tuấn","Trọng Hiếu","Phạm Hồng Phước","Vũ","JustaTee","BigDaddy","Karik","Binz","Suboi","Đen Vâu","Lil Tuấn Kiệt","B Ray","Rhymastic","Touliver","Hoaprox","Pháo","HIEUTHUHAI","Wren Evans","tlinh","MCK","GDucky","HURRYKNG","LOW G","Seachains"]

print("Đang tạo từ vựng...")

lines = set()

def add(h, a):
    lines.add(f"{h}|{a}")

# ---- Khối cũ (giữ nguyên) ----
for w in dong_vat:
    add("con...", f"con {w}")
    for t in tinh_tu:
        add("con...", f"con {w} {t}")
    for c in mau_sac:
        add("con...", f"con {w} màu {c}")
        add("con...", f"con {w} lông màu {c}")
    for kt in kich_thuoc:
        add("con...", f"con {w} {kt}")

for w in do_vat:
    add("cái...", f"cái {w}")
    for t in tinh_tu:
        add("cái...", f"cái {w} {t}")
    for v in vat_lieu:
        add("cái...", f"cái {w} bằng {v}")
    for c in mau_sac:
        add("cái...", f"cái {w} màu {c}")

for w in dia_diem:
    add("ở...", f"ở {w}")
    for t in tinh_tu[:30]:
        add("ở...", f"ở {w} {t}")
    for d in dia_diem:
        if d != w:
            add("ở...", f"ở {w} gần {d}")

for w in mau_sac:
    add("màu...", f"màu {w}")
    add("màu...", f"màu {w} đẹp")
    add("màu...", f"màu {w} đậm")
    add("màu...", f"màu {w} nhạt")
    add("màu...", f"màu {w} tươi")

for w in trai_cay:
    add("quả...", f"quả {w}")
    add("quả...", f"quả {w} chín")
    add("quả...", f"quả {w} xanh")
    add("quả...", f"quả {w} ngọt")
    add("quả...", f"quả {w} chua")
    for c in mau_sac[:15]:
        add("quả...", f"quả {w} màu {c}")
        add("quả...", f"quả {w} màu {c} chín")

for w in rau_cu:
    add("rau...", f"rau {w}")
    add("củ...", f"củ {w}")
    add("rau...", f"rau {w} tươi")
    add("rau...", f"rau {w} non")
    add("rau...", f"rau {w} già")
    add("rau...", f"rau {w} sạch")

for w in hoa:
    add("hoa...", f"hoa {w}")
    add("hoa...", f"hoa {w} đẹp")
    add("hoa...", f"hoa {w} thơm")
    for c in mau_sac[:20]:
        add("hoa...", f"hoa {w} màu {c}")

for w in hanh_dong:
    add("đang...", f"đang {w}")
    add("muốn...", f"muốn {w}")
    add("thích...", f"thích {w}")
    add("cần...", f"cần {w}")
    add("phải...", f"phải {w}")

for w in tinh_cam:
    add("cảm thấy...", f"cảm thấy {w}")
    add("rất...", f"rất {w}")
    add("hơi...", f"hơi {w}")
    add("cực kỳ...", f"cực kỳ {w}")
    add("vô cùng...", f"vô cùng {w}")

for w in nghe_nghiep:
    add("người...", f"người {w}")
    add("nghề...", f"nghề {w}")
    add("làm...", f"làm {w}")

for w in bo_phan:
    add("bộ phận...", f"{w}")
    add("cơ thể...", f"{w}")

for w in thoi_tiet:
    add("thời tiết...", f"trời {w}")
    add("trời...", f"trời {w}")
    add("hôm nay...", f"hôm nay trời {w}")

for w in am_thanh:
    add("nghe...", f"nghe {w}")
    add("tiếng...", f"{w}")

for w in mon_an:
    add("món...", f"món {w}")
    add("ăn...", f"ăn {w}")
    add("nấu...", f"nấu {w}")

for w in the_thao:
    add("chơi...", f"chơi {w}")
    add("môn...", f"môn {w}")
    add("tập...", f"tập {w}")

for w in phuong_tien:
    add("đi...", f"đi {w}")
    add("xe...", f"{w}")
    add("phương tiện...", f"{w}")

for w in vat_lieu:
    add("bằng...", f"bằng {w}")
    add("chất liệu...", f"{w}")

for w in hinh_dang:
    add("hình...", f"hình {w}")
    add("có dạng...", f"{w}")

for w in kich_thuoc:
    add("kích thước...", f"{w}")
    add("rất...", f"rất {w}")

for w in gia_vi:
    add("gia vị...", f"{w}")
    add("nêm...", f"nêm {w}")

for w in dung_cu:
    add("dụng cụ...", f"{w}")
    add("đồ nghề...", f"{w}")

for w in thiet_bi:
    add("thiết bị...", f"{w}")
    add("máy...", f"{w}")

for w in do_uong:
    add("uống...", f"uống {w}")
    add("đồ uống...", f"{w}")

for w in thuc_vat:
    add("cây...", f"cây {w}")
    add("thực vật...", f"{w}")

for w in nha_cua:
    add("nhà...", f"nhà có {w}")
    add("xây...", f"xây {w}")

for w in con_vat_bien:
    add("con...", f"con {w}")
    add("dưới biển có...", f"con {w}")

for w in cach_dien_dat:
    add("cách nói...", f"{w} đẹp")
    add("cách nói...", f"{w} hay")

for w in tinh_tu:
    add("tính từ...", f"{w}")

# ---- Khối mở rộng (chủ đề mới) ----
for w in do_choi:
    add("đồ chơi...", f"đồ chơi {w}")
    add("trẻ em thích...", f"{w}")
    for c in mau_sac[:15]:
        add("đồ chơi...", f"đồ chơi {w} màu {c}")

for w in nhac_cu:
    add("nhạc cụ...", f"{w}")
    add("chơi...", f"chơi {w}")
    add("nghe...", f"nghe {w}")

for w in vu_khi:
    add("vũ khí...", f"{w}")
    add("cầm...", f"cầm {w}")
    add("chiến đấu bằng...", f"{w}")

for w in do_trang_suc:
    add("trang sức...", f"{w}")
    add("đeo...", f"đeo {w}")
    add("tặng...", f"tặng {w}")

for w in benh_tat:
    add("bệnh...", f"bệnh {w}")
    add("bị...", f"bị {w}")
    add("mắc...", f"mắc {w}")

for w in trieu_chung:
    add("triệu chứng...", f"{w}")
    add("cảm thấy...", f"{w}")

for w in hành_tinh_sao:
    add("thiên văn...", f"{w}")
    add("quan sát...", f"{w}")
    add("nhìn thấy...", f"{w}")

for w in nguyen_to:
    add("nguyên tố...", f"{w}")
    add("hóa học...", f"{w}")

for w in quoc_gia:
    add("quốc gia...", f"{w}")
    add("đi...", f"đi {w}")
    add("sống ở...", f"{w}")

for w in tinh_thanh:
    add("tỉnh...", f"tỉnh {w}")
    add("thành phố...", f"thành phố {w}")
    add("đi...", f"đi {w}")

for w in le_hoi:
    add("lễ hội...", f"{w}")
    add("tổ chức...", f"tổ chức {w}")
    add("dự...", f"dự {w}")

for w in tro_choi_dan_gian:
    add("trò chơi...", f"{w}")
    add("chơi...", f"chơi {w}")
    add("trẻ em chơi...", f"{w}")

for w in do_an_vat:
    add("đồ ăn vặt...", f"{w}")
    add("ăn...", f"ăn {w}")
    add("mua...", f"mua {w}")

for w in linh_kien_may:
    add("linh kiện...", f"{w}")
    add("lắp...", f"lắp {w}")

for w in ung_dung_web:
    add("ứng dụng...", f"{w}")
    add("dùng...", f"dùng {w}")
    add("mở...", f"mở {w}")

for w in game:
    add("game...", f"{w}")
    add("chơi...", f"chơi {w}")
    add("tải...", f"tải {w}")

for w in bo_phim:
    add("phim...", f"{w}")
    add("xem...", f"xem {w}")

for w in ca_si:
    add("ca sĩ...", f"{w}")
    add("nghe...", f"nghe {w} hát")

# ---- Tổ hợp chéo để tăng dung lượng ----
for a in dong_vat:
    for b in mau_sac[:30]:
        add("con...", f"con {a} màu {b} đẹp")
    for b in tinh_tu[:40]:
        add("con...", f"con {a} rất {b}")
    for b in kich_thuoc[:20]:
        add("con...", f"con {a} {b} đáng yêu")

for a in do_vat:
    for b in vat_lieu[:30]:
        add("cái...", f"cái {a} làm bằng {b} đẹp")
    for b in mau_sac[:30]:
        add("cái...", f"cái {a} màu {b} mới")
    for b in tinh_tu[:30]:
        add("cái...", f"cái {a} rất {b}")

for a in trai_cay:
    for b in mau_sac[:20]:
        add("quả...", f"quả {a} màu {b}")
        add("quả...", f"quả {a} chín màu {b}")

for a in rau_cu:
    for b in mau_sac[:15]:
        add("rau...", f"rau {a} màu {b}")
        add("củ...", f"củ {a} màu {b}")

for a in hoa:
    for b in mau_sac:
        add("hoa...", f"hoa {a} màu {b} đẹp")
        add("hoa...", f"hoa {a} màu {b} thơm")

for a in do_choi:
    for b in mau_sac[:20]:
        add("đồ chơi...", f"đồ chơi {a} màu {b}")

for a in nhac_cu:
    for b in tinh_tu[:30]:
        add("nhạc cụ...", f"{a} {b}")

for a in mon_an:
    for b in gia_vi[:30]:
        add("món...", f"{a} nêm {b}")
        add("món...", f"{a} có {b}")

for a in do_uong:
    for b in trai_cay[:30]:
        add("đồ uống...", f"{a} vị {b}")
        add("đồ uống...", f"{a} làm từ {b}")

for a in the_thao:
    for b in tinh_cam[:30]:
        add("môn...", f"{a} rất {b}")

for a in nghe_nghiep:
    for b in tinh_cam:
        add("người...", f"người {a} rất {b}")

for a in bo_phan:
    for b in tinh_tu[:30]:
        add("bộ phận...", f"{a} {b}")

for a in quoc_gia:
    for b in mon_an[:40]:
        add("quốc gia...", f"{a} có món {b}")
    for b in le_hoi[:20]:
        add("quốc gia...", f"{a} có {b}")

for a in tinh_thanh:
    for b in mon_an[:30]:
        add("tỉnh...", f"{a} có món {b}")
    for b in dia_diem[:30]:
        add("tỉnh...", f"{a} có {b}")

for a in benh_tat:
    for b in trieu_chung[:30]:
        add("bệnh...", f"{a} có triệu chứng {b}")

for a in am_thanh:
    for b in dia_diem[:30]:
        add("nghe...", f"nghe {a} ở {b}")

for a in phuong_tien:
    for b in dia_diem[:30]:
        add("đi...", f"đi {a} đến {b}")

for a in thiet_bi:
    for b in vat_lieu[:20]:
        add("thiết bị...", f"{a} làm bằng {b}")

with open("words.txt", "w", encoding="utf-8") as f:
    for line in sorted(lines):
        f.write(line + "\n")

size_kb = os.path.getsize("words.txt") / 1024
print(f"✅ Đã tạo {len(lines)} dòng | Kích thước: {size_kb:.1f} KB"))} dòng | Kích thước: {size_kb:.1f} KB")ích thước: {size_kb:.1f} KB")
