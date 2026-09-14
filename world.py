import itertools

dong_vat = ["chó","mèo","voi","hổ","rắn","cá","gà","vịt","heo","bò","trâu","ngựa","dê","cừu","khỉ","gấu","thỏ","chuột","sư tử","báo","hươu","nai","cáo","sói","hạc","đại bàng","chim","cú","bướm","ong","kiến","muỗi","ruồi","gián","nhện","bọ cạp","tôm","cua","ốc","mực","bạch tuộc","cá sấu","rùa","ếch","nhái","thằn lằn","tắc kè","kỳ đà","hải cẩu","cá voi","cá heo","chim ưng","bồ câu","yến","thiên nga","ngỗng","vẹt","đà điểu","khủng long","sứa","sao biển","hà mã","tê giác","hươu cao cổ","linh cẩu","sóc","nhím","mối","mọt","châu chấu","chuồn chuồn","bọ ngựa","bọ xít","đom đóm","cá mập","cá ngựa","cá hồi","cá rô","cá chép","cá vàng","cá trê","cá lóc","cá basa","gà trống","gà mái","gà con","vịt xiêm","vịt trời","ngan","công","trĩ","gà tây","chó sói","chó ngao","chó poodle","mèo tam thể","mèo mun","mèo mướp","mèo Ba Tư","khỉ đột","tinh tinh","đười ươi","gấu trúc","gấu bắc cực","gấu nâu","cáo tuyết","sư tử biển","hải mã","cá đuối","cá kiếm","cá ngừ","cá thu","cá chỉ vàng","cá cảnh","cá diêu hồng","cá lia thia","cá betta","cá la hán","cá rồng","cá đĩa","cá tỳ bà","cá chuột","cá mún","cá bảy màu","tép","tôm hùm","tôm sú","tôm càng","ghẹ","hàu","nghêu","sò","trai","bào ngư","hải sâm","nhum","mực ống","mực nang","bạch tuộc đốm","sao biển đỏ","san hô","huệ biển","hải quỳ"]

do_vat = ["bàn","ghế","quạt","tivi","điện thoại","máy tính","tủ","giường","gối","chăn","màn","ly","cốc","chén","bát","đĩa","muỗng","thìa","nĩa","đũa","nồi","chảo","mâm","rổ","bao","túi","bóp","ví","cặp","nón","mũ","áo","quần","váy","khăn","nhẫn","đồng hồ","gương","lược","kéo","dao","búa","đinh","chìa khóa","ổ khóa","ô","dù","chổi","thau","xô","máy giặt","tủ lạnh","máy lạnh","lò vi sóng","bếp","xe đạp","xe máy","ô tô","tàu thủy","máy bay","bút","thước","tập","sách","vở","đèn","pin","sạc","tai nghe","loa","micro","camera","máy ảnh","bóng đèn","quạt trần","điều hòa","nồi cơm","ấm siêu tốc","bàn ủi","máy hút bụi","máy sấy","máy xay","máy ép","nồi chiên","lò nướng","bếp ga","bếp từ","chén trà","ly nước","bình hoa","chậu cây","thảm","rèm","cửa","cửa sổ","cầu thang","ban công","sân","tường","mái nhà","gạch","ngói","xi măng","cát","đá","gỗ","sắt","thép","nhôm","đồng","chì","kẽm","vàng","bạc","bạch kim","kim cương","đá quý","ngọc trai","san hô","hổ phách","pha lê","thủy tinh","nhựa","cao su","vải","len","lụa","gấm","nhung","da","giấy","bìa","carton","xốp","mút","keo","băng dính","dây thun","dây thừng","dây điện","ổ cắm","công tắc","cầu dao","aptomat","biến áp","mô tơ","động cơ","máy bơm","máy nén","máy phát","quạt hút","quạt thông gió","máy lọc nước","máy nước nóng","bồn cầu","chậu rửa","vòi nước","sen tắm","bồn tắm","lavabo","gương soi","kệ","tủ giày","móc áo","phơi đồ","bàn chải","kem đánh răng","xà bông","dầu gội","sữa tắm","khăn tắm","khăn mặt","bàn là","cây lau nhà","cây chổi","cây gậy","cây búa","cây kéo","cây bút","cây thước","cây nến","cây quạt","cây đàn","cây sáo","cây kèn","cây trống"]

dia_diem = ["trường học","bệnh viện","nhà","công viên","siêu thị","chợ","rạp chiếu phim","nhà hàng","quán ăn","quán cà phê","sân bay","nhà ga","bến xe","bãi biển","trên núi","trong rừng","ngã tư","văn phòng","công ty","nhà máy","công trường","thư viện","nhà sách","phòng tập","hồ bơi","khách sạn","tiệm hớt tóc","ngân hàng","bưu điện","phòng ngủ","phòng khách","nhà bếp","sân vườn","ban công","tầng hầm","sân thượng","gara","nhà kho","nhà xe","bãi đỗ xe","trạm xăng","trạm xe buýt","bến tàu","bến phà","cảng biển","sân vận động","nhà thi đấu","cung văn hóa","nhà hát","bảo tàng","triển lãm","đền","chùa","nhà thờ","miếu","lăng","nghĩa trang","công viên nước","khu vui chơi","vườn thú","vườn bách thảo","khu bảo tồn","trại hè","trại giam","đồn công an","trụ sở","tòa án","quốc hội","phủ chủ tịch","đại sứ quán","lãnh sự quán","biên giới","cửa khẩu","hải quan","trạm thu phí","cầu","hầm","đèo","eo biển","vịnh","vũng","đầm","hồ","sông","suối","thác","ao","giếng","kênh","mương","rạch","bờ biển","bờ sông","bờ hồ","đảo","bán đảo","quần đảo","núi lửa","hang động","thung lũng","cao nguyên","đồng bằng","sa mạc","ốc đảo","thảo nguyên","rừng nhiệt đới","rừng nguyên sinh","rừng ngập mặn"]

mau_sac = ["đỏ","xanh","xanh lá","xanh dương","xanh trời","xanh biển","xanh ngọc","xanh rêu","xanh lá mạ","xanh lục","xanh lam","xanh chàm","vàng","vàng chanh","vàng cam","vàng nghệ","vàng tươi","vàng đất","tím","tím than","tím hoa cà","tím lavender","hồng","hồng nhạt","hồng đậm","hồng phấn","hồng sen","cam","cam đất","cam cháy","đen","đen tuyền","đen bóng","đen mờ","trắng","trắng sữa","trắng ngà","trắng tinh","trắng xám","xám","xám tro","xám bạc","xám khói","nâu","nâu đất","nâu gỗ","nâu chocolate","nâu cà phê","kem","kem sữa","bạc","đồng","đồng đỏ","đồng thau","chanh","chàm","ngọc","rêu","hổ phách","san hô","tràm","đỏ đô","đỏ tươi","đỏ thẫm","đỏ son","đỏ rượu vang","đỏ gạch","đỏ cam"]

trai_cay = ["táo","chuối","cam","dưa hấu","xoài","ổi","mận","đào","nho","dâu","dừa","dứa","khóm","đu đủ","sầu riêng","măng cụt","vải","nhãn","chôm chôm","mãng cầu","lựu","mắc ca","óc chó","hồng","sung","vú sữa","sapoche","bơ","thanh long","kiwi","cherry","dâu tây","việt quất","mâm xôi","phúc bồn tử","lý gai","me","táo tàu","táo mèo","táo gai","sung mỹ","đào tiên","chà là","ô liu","hạnh nhân","hạt dẻ","hạt điều","hạt bí","hạt hướng dương","hạt dưa"]

rau_cu = ["cải","cải ngọt","cải xanh","cải bó xôi","cải thìa","cải cúc","cải xoăn","rau muống","rau ngót","rau dền","rau mồng tơi","rau đay","rau rút","rau cần","rau ngò","rau mùi","rau húng","rau quế","rau tía tô","rau kinh giới","rau diếp cá","rau xà lách","rau bắp cải","bắp cải trắng","bắp cải tím","bông cải","súp lơ","cà rốt","củ cải","củ dền","su hào","khoai tây","khoai lang","khoai môn","khoai sọ","khoai mì","sắn","củ năng","củ sen","củ gừng","củ nghệ","củ tỏi","củ hành","hành lá","hành tím","hành tây","ớt","ớt chuông","cà chua","cà tím","cà pháo","đậu bắp","đậu cô ve","đậu hà lan","đậu que","đậu đũa","bí đỏ","bí xanh","bí đao","mướp","mướp đắng","khổ qua","dưa leo","dưa chuột","dưa gang","dưa hồng","giá đỗ","măng tây","măng tre","nấm rơm","nấm mèo","nấm hương","nấm kim châm","nấm đùi gà","nấm bào ngư","nấm đông cô","ngó sen","rau mầm","rau thơm","rau sống","rau luộc","rau xào","rau trộn"]

hoa = ["hồng","cúc","lan","huệ","loa kèn","ly","tuylip","thủy tiên","lay ơn","cẩm chướng","đồng tiền","sao","thược dược","trạng nguyên","mào gà","sen","súng","dâm bụt","phượng","bằng lăng","muồng","điệp","giấy","xuyến chi","bồ công anh","cỏ may","cỏ ba lá","hướng dương","cẩm tú cầu","tử đằng","anh đào","đào","mơ","mai","quỳnh","dạ lý hương","nhài","mộc","hoàng lan","ngọc lan","sứ","đại","lan hồ điệp","lan vũ nữ","lan hài","lan quế","hồng leo","hồng cổ","hồng bạch","hồng nhung","hồng vàng","hồng xanh"]

hanh_dong = ["ăn","uống","ngủ","chơi","học","làm","chạy","đi","hát","múa","nhảy","vẽ","viết","đọc","nghe","nói","xem","cười","khóc","suy nghĩ","tìm kiếm","lập trình","mua sắm","nấu ăn","dọn dẹp","tắm rửa","lái xe","đi bộ","leo núi","bơi lội","đạp xe","chạy bộ","tập yoga","tập gym","đá bóng","đánh cầu","chơi cờ","chơi game","xem phim","nghe nhạc","đọc sách","viết thư","gọi điện","nhắn tin","học bài","làm bài","thi cử","phỏng vấn","họp","thuyết trình","giảng bài","chữa bệnh","khám bệnh","bán hàng","mua hàng","trả tiền","tiết kiệm","đầu tư","vay mượn","cho vay","tặng quà","nhận quà","chụp ảnh","quay phim","vẽ tranh","điêu khắc","nấu cơm","rửa chén","lau nhà","giặt đồ","phơi đồ","ủi đồ","gấp đồ","đan lát","may vá","thêu thùa","đóng giày","sửa xe","sửa điện","sửa nước","xây nhà","đổ bê tông","trồng cây","tưới cây","cắt cỏ","hái quả","câu cá","săn bắn","chăn nuôi","gieo hạt","gặt lúa"]

tinh_cam = ["vui","buồn","mệt","đói","khát","tức giận","hạnh phúc","lo lắng","sợ hãi","bất ngờ","bình tĩnh","tự tin","thông minh","dũng cảm","tốt bụng","hiền lành","vui vẻ","nhiệt tình","chăm chỉ","trung thực","kiên nhẫn","sáng tạo","thấu hiểu","hào hứng","phấn khích","thư giãn","căng thẳng","hồi hộp","ngạc nhiên","xúc động","cảm động","biết ơn","hối hận","ghen tị","ghen tuông","ghen ghét","yêu thương","thương xót","đồng cảm","tôn trọng","khinh bỉ","coi thường","tự hào","khiêm tốn","kiêu ngạo","ích kỷ","vị tha","nhân hậu","độc ác","hung dữ","hiếu thảo","bất hiếu","trung thành","phản bội","thật thà","dối trá","ngây thơ","khờ khạo","lanh lợi","nhanh nhẹn","chậm chạp","lười biếng","siêng năng","cần cù","chịu khó","chịu thương","chịu khổ","lạc quan","bi quan","yêu đời","chán đời","mệt mỏi","sảng khoái","khỏe khoắn","ốm yếu","đau đớn","sung sướng","khổ sở","vất vả","nhàn nhã","rảnh rỗi","bận rộn"]

nghe_nghiep = ["bác sĩ","y sĩ","y tá","giáo viên","học sinh","sinh viên","kỹ sư","lập trình viên","họa sĩ","ca sĩ","diễn viên","thợ may","thợ mộc","thợ điện","thợ hàn","thợ xây","đầu bếp","phi công","tiếp viên","cảnh sát","bộ đội","nông dân","ngư dân","lâm tặc","thợ săn","thợ lặn","thợ mỏ","thợ sơn","thợ nề","thợ đá","thợ bạc","thợ vàng","thợ gốm","thợ nhuộm","thợ dệt","thợ in","thợ chụp ảnh","thợ quay phim","thợ trang điểm","thợ làm tóc","thợ làm móng","nhân viên bán hàng","nhân viên thu ngân","nhân viên phục vụ","nhân viên giao hàng","tài xế taxi","tài xế xe bus","tài xế xe tải","trưởng phòng","giám đốc","chủ tịch","thư ký","kế toán","luật sư","thẩm phán","công tố viên","kiểm sát viên","công chứng viên","nhà báo","phóng viên","biên tập viên","nhà văn","nhà thơ","nhà báo","nhà nghiên cứu","giáo sư","tiến sĩ","thạc sĩ","nghiên cứu sinh","dược sĩ","nha sĩ","bác sĩ thú y","nhà tâm lý học","nhà xã hội học","nhà kinh tế","nhà ngoại giao","nhà chính trị","nhà quân sự","cảnh sát trưởng","đội trưởng","trung úy","thượng úy","đại úy","thiếu tá","trung tá","thượng tá","đại tá","tướng"]

bo_phan = ["đầu","tóc","trán","mắt","lông mày","lông mi","mũi","miệng","môi","răng","lưỡi","cằm","má","tai","cổ","vai","ngực","bụng","lưng","eo","hông","mông","đùi","đầu gối","bắp chân","cẳng chân","cổ chân","bàn chân","ngón chân","cánh tay","cùi chỏ","cổ tay","bàn tay","ngón tay","móng tay","da","thịt","xương","máu","tim","phổi","gan","thận","dạ dày","ruột","tụy","lá lách","túi mật","não","tủy","dây thần kinh","mạch máu","tĩnh mạch","động mạch","cơ","gân","sụn","khớp","răng nanh","răng cửa","răng hàm","răng khôn","lợi","vòm miệng","thực quản","khí quản","phế quản","ruột non","ruột già","trực tràng","bàng quang","niệu quản","tuyến giáp","tuyến thượng thận","tuyến yên","tuyến tụy","tuyến nước bọt","tuyến mồ hôi","tuyến sữa"]

thoi_tiet = ["nắng","mưa","gió","bão","lốc","sấm","sét","mây","mù","sương","tuyết","mưa đá","mưa phùn","mưa rào","mưa dông","mưa ngâu","mưa bão","nắng đẹp","nắng nóng","nắng gắt","nắng chói","âm u","u ám","râm mát","mát mẻ","se lạnh","lạnh giá","rét đậm","rét hại","nóng bức","oi bức","oi ả","hanh khô","ẩm ướt","ngột ngạt","trong lành","trong xanh","quang đãng","đẹp trời","xấu trời","thất thường","khắc nghiệt","dễ chịu","khó chịu"]

am_thanh = ["tiếng nói","tiếng cười","tiếng khóc","tiếng hát","tiếng đàn","tiếng sáo","tiếng trống","tiếng kèn","tiếng vĩ cầm","tiếng piano","tiếng guitar","tiếng sáo diều","tiếng chim hót","tiếng gà gáy","tiếng chó sủa","tiếng mèo kêu","tiếng vịt kêu","tiếng bò rống","tiếng hổ gầm","tiếng sói hú","tiếng voi rống","tiếng ngựa hí","tiếng dế mèn","tiếng ve sầu","tiếng ếch nhái","tiếng côn trùng","tiếng mưa rơi","tiếng gió thổi","tiếng sóng vỗ","tiếng thác đổ","tiếng suối chảy","tiếng sấm rền","tiếng sét đánh","tiếng nổ","tiếng súng","tiếng pháo","tiếng còi","tiếng chuông","tiếng trống trường","tiếng bước chân","tiếng gõ cửa","tiếng vỗ tay","tiếng huýt sáo","tiếng thì thầm","tiếng hò hét","tiếng la hét","tiếng gào thét"]

mon_an = ["phở","bún","miến","mì","hủ tiếu","bánh canh","bánh đa","bánh cuốn","bánh xèo","bánh khọt","bánh bèo","bánh bột lọc","bánh ướt","bánh chưng","bánh tét","bánh giò","bánh bao","bánh mì","bánh ngọt","bánh kem","bánh quy","bánh bông lan","bánh trung thu","bánh flan","bánh pudding","chè","chè đậu","chè ba màu","chè thái","chè khúc bạch","xôi","xôi gấc","xôi đậu","xôi mặn","cơm","cơm tấm","cơm rang","cơm chiên","cơm gà","cơm sườn","cơm bụi","cơm hến","cơm âm phủ","cháo","cháo lòng","cháo gà","cháo cá","cháo vịt","cháo hến","cháo đậu","canh","canh chua","canh bí","canh rau","canh khổ qua","súp","súp gà","súp cua","súp măng cua","salad","salad trộn","salad rau","gỏi","gỏi cuốn","gỏi bò","gỏi gà","nem","nem chua","nem nướng","chả","chả giò","chả cá","chả lụa","chả trứng","thịt nướng","thịt kho","thịt xào","thịt luộc","thịt quay","thịt chó","thịt mèo","thịt bò","thịt heo","thịt gà","thịt vịt","thịt dê","thịt cừu","cá chiên","cá hấp","cá kho","cá nướng","cá luộc","cá rán","tôm chiên","tôm hấp","tôm nướng","mực xào","mực chiên","mực nướng","lẩu","lẩu thái","lẩu nấm","lẩu bò","lẩu hải sản","nướng","nướng than","nướng giấy bạc","chiên","xào","hấp","luộc","kho","rim","nấu","nấu canh","nấu cháo","nấu cơm","nấu lẩu"]

the_thao = ["bóng đá","bóng rổ","bóng chuyền","bóng bàn","bóng ném","bóng nước","bóng chày","bóng bầu dục","cầu lông","quần vợt","bơi lội","điền kinh","chạy marathon","chạy việt dã","đua xe","đua ngựa","đua thuyền","đua xe đạp","thể dục dụng cụ","gym","yoga","aerobic","karate","judo","taekwondo","vovinam","võ cổ truyền","boxing","muay thái","vật","cử tạ","bắn cung","bắn súng","cưỡi ngựa","leo núi","trượt tuyết","trượt băng","lướt sóng","lướt ván","nhảy dù","nhảy cầu","đánh golf","đánh cờ","đánh bài","đấu kiếm","đá cầu","nhảy dây","kéo co","nhảy xa","nhảy cao","đẩy gậy","ném đĩa","ném lao","tạ","cử tạ","cầu mây","pickleball","pickleball","bóng chuyền bãi biển","bóng đá mini","futsal","bóng rổ 3x3"]

phuong_tien = ["xe đạp","xe máy","xe ôm","xe taxi","xe buýt","xe tải","xe container","xe khách","xe du lịch","xe cứu thương","xe cứu hỏa","xe cảnh sát","xe tang","xe ba gác","xe lam","xe xích lô","xe lôi","xe kéo","xe bò","xe ngựa","tàu hỏa","tàu điện","tàu điện ngầm","tàu cao tốc","tàu thủy","tàu du lịch","tàu ngầm","tàu sân bay","tàu chiến","tàu cá","tàu vũ trụ","phi thuyền","máy bay","máy bay phản lực","máy bay trực thăng","máy bay ném bom","máy bay tiêm kích","tên lửa","vệ tinh","trạm không gian","khinh khí cầu","dù lượn","mô tô","mô tô phân khối lớn","xế hộp","xế độ","xế cổ","siêu xe","xe thể thao","xe limousine"]

vat_lieu = ["gỗ","gỗ tự nhiên","gỗ công nghiệp","sắt","thép","gang","nhôm","đồng","đồng đỏ","đồng thau","chì","kẽm","thiếc","vàng","bạc","bạch kim","kim cương","đá quý","ruby","sapphire","emerald","ngọc trai","san hô","hổ phách","pha lê","thủy tinh","nhựa","nhựa PVC","nhựa PE","nhựa ABS","cao su","cao su non","vải","vải cotton","vải lụa","vải len","vải dạ","vải nhung","vải gấm","vải kaki","vải jean","vải thô","vải voan","da","da bò","da cá sấu","da trăn","da cừu","da nhân tạo","giấy","bìa","carton","giấy báo","giấy vệ sinh","giấy ăn","xốp","mút","mút xốp","keo","keo dán","keo nến","băng dính","băng keo","gốm","sứ","đất sét","đất nung","xi măng","bê tông","gạch","ngói","đá","đá hoa cương","đá cẩm thạch","đá granite","đá marble","thạch cao","amiăng","carbon","sợi thủy tinh","sợi carbon","sợi tổng hợp","kim loại","hợp kim","inox","titan"]

hinh_dang = ["tròn","vuông","chữ nhật","tam giác","lục giác","bát giác","ngũ giác","thất giác","bầu dục","oval","elip","parabol","hyperbol","xoắn ốc","lượn sóng","gợn sóng","hình tim","hình sao","hình trăng","hình hoa","hình lá","hình cầu","hình trụ","hình nón","hình chóp","hình hộp","hình lập phương","hình thoi","hình bình hành","hình thang","hình quạt","hình vành khuyên","hình xuyến","hình xoắn","hình phễu","hình giọt nước","hình yên ngựa","hình móng ngựa","hình chữ S","hình chữ U","hình chữ V","hình chữ X","hình chữ Y","hình chữ Z","hình chữ O"]

kich_thuoc = ["khổng lồ","to lớn","vĩ đại","đồ sộ","hoành tráng","bự","to","lớn","vừa","trung bình","nhỏ","bé","nhỏ xíu","tí hon","tí xíu","li ti","nhỏ nhắn","thon gọn","mảnh khảnh","thon thả","mập mạp","béo tốt","tròn trịa","mũm mĩm","gầy guộc","ốm nhom","cao","cao lớn","cao ráo","lùn","thấp","thấp bé","dài","ngắn","rộng","hẹp","dày","mỏng","nặng","nhẹ","sâu","nông","xa","gần"]

gia_vi = ["muối","đường","tiêu","ớt","tỏi","hành","gừng","nghệ","sả","riềng","quế","hồi","đinh hương","thảo quả","hạt mùi","hạt thì là","hạt cần tây","hạt nhục đậu khấu","bột ngọt","bột nêm","hạt nêm","nước mắm","nước tương","xì dầu","dầu hào","tương ớt","tương cà","mayonnaise","mù tạt","wasabi","giấm","giấm táo","giấm gạo","rượu","rượu vang","rượu trắng","bia","cà phê","trà","mật ong","siro","chanh","quất","tắc","me","tamarind","ớt bột","ớt tươi","ớt khô","ớt hiểm","ớt chỉ thiên","ớt chuông","ớt bột Hàn","ớt bột Ấn"]

dung_cu = ["búa","đục","cưa","khoan","máy khoan","máy cắt","máy mài","máy hàn","máy tiện","máy phay","máy bào","máy đục","máy đánh bóng","máy nén khí","máy bơm nước","máy phát điện","máy hút bụi","máy thổi lá","máy cắt cỏ","máy xới đất","máy trộn bê tông","máy đầm","máy xúc","máy ủi","máy cẩu","xe rùa","xẻng","cuốc","cào","liềm","hái","rựa","dao phay","dao thái","dao gọt","dao rọc giấy","dao cạo","dao lam","bàn chải sắt","giũa","dũa","đe","kìm","cờ lê","mỏ lết","tua vít","vít","ốc","bu lông","đai ốc","vòng đệm","long đền","chốt","chìa vặn","cưa tay","cưa máy","cưa lọng","cưa xích","đinh","đinh vít","ghim","kẹp","kẹp giấy","kẹp gỗ","băng đô"]

thiet_bi = ["máy tính bàn","laptop","máy tính bảng","smartphone","smartwatch","smart TV","tivi","máy chiếu","loa bluetooth","loa kéo","tai nghe","tai nghe chụp tai","tai nghe nhét tai","tai nghe bluetooth","micro","ampli","receiver","đầu đĩa","đầu karaoke","amly karaoke","cục đẩy công suất","máy ảnh DSLR","máy ảnh mirrorless","máy ảnh compact","máy quay phim","flycam","webcam","máy in","máy scan","máy photocopy","máy fax","máy hủy tài liệu","máy đếm tiền","máy chấm công","máy tính tiền","máy in hóa đơn","máy pos","máy quét mã vạch","máy in mã vạch","máy đọc thẻ","máy rút tiền ATM","máy đổi tiền","máy bán nước tự động","máy bán hàng tự động","máy massage","máy đo huyết áp","máy đo đường huyết","máy đo nhiệt độ","máy đo nhịp tim","máy đo nồng độ oxy","máy trợ thính","máy khử trùng","máy tạo ẩm","máy hút ẩm","máy lọc không khí","máy sưởi","máy nước nóng","máy nước lạnh"]

do_uong = ["nước lọc","nước khoáng","nước tinh khiết","nước suối","nước ngọt","nước có ga","nước cam","nước chanh","nước dừa","nước mía","nước ép táo","nước ép cà rốt","nước ép cần tây","nước ép cà chua","nước ép thơm","nước ép ổi","nước ép nho","nước ép lựu","sinh tố bơ","sinh tố xoài","sinh tố chuối","sinh tố dâu","sinh tố mãng cầu","sữa tươi","sữa chua","sữa đặc","sữa bột","sữa đậu nành","sữa gạo","sữa hạt","sữa yến mạch","sữa hạnh nhân","sữa óc chó","cà phê đen","cà phê sữa","cà phê muối","cà phê trứng","bạc xỉu","trà đá","trà nóng","trà xanh","trà đen","trà ô long","trà sen","trà hoa cúc","trà hoa hồng","trà gừng","trà sữa","trà sữa trân châu","trà sữa matcha","trà sữa thái","trà trái cây","trà đào","trà vải","trà chanh","trà tắc","bia","bia hơi","bia lon","bia chai","rượu vang đỏ","rượu vang trắng","rượu sâm banh","rượu whisky","rượu vodka","rượu rum","rượu tequila","rượu mơ","rượu nếp","rượu cần"]

thuc_vat = ["lúa","ngô","khoai","sắn","đậu","mè","vừng","lạc","hướng dương","cà phê","ca cao","chè","hồ tiêu","điều","cao su","dừa","cau","trầu","tre","trúc","nứa","bương","vầu","hóp","lồ ô","dừa nước","bần","đước","mắm","sú","vẹt","dà","cóc","gừa","phi lao","keo","bạch đàn","thông","tùng","bách","xà cừ","lim","sến","gõ đỏ","gụ","cẩm lai","trắc","sưa","giáng hương","hoàng đàn","pơ mu","sa mộc","thông đỏ","thông năm lá","tuế","vạn tuế","dương xỉ","rêu","địa y","tảo","rong","rong biển","rong mơ","rong nho","rong câu","bèo","bèo tấm","bèo lục bình","sen","súng","rau dừa nước","cỏ","cỏ voi","cỏ voi","cỏ lông chông","cỏ gà","cỏ may","cỏ chỉ"]

nha_cua = ["cửa chính","cửa phụ","cửa sổ","cửa sổ trời","cửa kính","cửa gỗ","cửa sắt","cửa cuốn","cửa xếp","cửa tự động","cửa xoay","cửa lùa","cửa nhôm","cửa nhựa","cửa chống cháy","cửa chống trộm","cửa cách âm","cửa cách nhiệt","cửa vòm","cửa hai cánh","cửa bốn cánh","cửa sổ chớp","cửa sổ lùa","cửa sổ mở hất","cửa sổ mở quay","cửa sổ mở trượt","lan can","ban công","sân thượng","sân trước","sân sau","hiên nhà","mái hiên","mái bằng","mái tôn","mái ngói","mái lá","mái thái","mái nhật","mái ngói âm dương","tường","tường gạch","tường bê tông","tường đá","tường gỗ","tường kính","tường ngăn","tường chịu lực","tường cách âm","tường cách nhiệt","tường trang trí","tường ốp gỗ","tường ốp đá","tường ốp gạch","tường sơn nước","tường giấy dán","cầu thang","cầu thang xoắn","cầu thang thẳng","cầu thang chữ L","cầu thang chữ U","cầu thang bộ","cầu thang máy","cầu thang gỗ","cầu thang sắt","cầu thang inox","cầu thang bê tông","cầu thang đá","cầu thang kính"]

con_vat_bien = ["cá heo","cá voi xanh","cá voi sát thủ","cá nhà táng","cá mập trắng","cá mập hổ","cá mập đầu búa","cá đuối điện","cá đuối ó","cá đuối bồng","cá ngừ đại dương","cá kiếm","cá buồm","cá cờ","cá thu ngừ","cá trích","cá cơm","cá mòi","cá nục","cá hồng","cá mú","cá chẽm","cá song","cá bớp","cá giò","cá đé","cá đù","cá lượng","cá hố","cá lịch","cá chình","cá lươn","cá trạch","cá kèo","cá bống","cá thòi lòi","cá rô đồng","cá rô phi","cá diêu hồng","cá điêu hồng","cá chim trắng","cá chim đen","cá ba sa","cá tra","cá basa","cá trắm","cá mè","cá chép","cá vàng","cá rồng","cá la hán","cá betta","cá bảy màu","cá đĩa","cá tỳ bà","cá chuột","cá mún","cá kiếm","cá hồi","cá tầm","cá hồi vân","cá hồi đỏ","cá trê","cá trê vàng","cá trê trắng","cá nheo","cá ngát","cá úc","cá chỉ vàng","cá phèn","cá liệt","cá móm","cá đối","cá khoai","cá bạc má","cá miễn sành"]

cach_dien_dat = ["rất","quá","lắm","cực kỳ","vô cùng","hết sức","siêu","thật","thiệt","cực","khá","hơi","hơi hơi","tương đối","hơi bị","khá là","có vẻ","dường như","hình như","chắc là","chắc hẳn","đúng là","quả nhiên","thực sự","thật sự","đích thực","chính hiệu","hàng thật","hàng xịn","hàng hiệu","cao cấp","sang trọng","quý phái","bình dân","dân dã","đơn giản","mộc mạc","giản dị","cầu kỳ","tinh tế","tinh xảo","khéo léo","tài tình","điêu luyện","siêu phàm","tuyệt vời","tuyệt hảo","hoàn hảo","hoàn mỹ","vô địch","bất bại","bất hủ","vĩnh cửu","trường tồn"]

tinh_tu = ["đẹp","xấu","to","nhỏ","bé","lớn","khổng lồ","nhỏ xíu","mới","cũ","nhanh","chậm","khỏe","yếu","cao","thấp","dài","ngắn","rộng","hẹp","nặng","nhẹ","nóng","lạnh","ấm","mát","mềm","cứng","sắc","cùn","tròn","vuông","đắt","rẻ","đẹp đẽ","xinh xắn","dễ thương","đáng yêu","đáng mến","thú vị","nhàm chán","hấp dẫn","lôi cuốn","mê hoặc","quyến rũ","thanh lịch","sang trọng","quý phái","bình dị","mộc mạc","giản dị","tinh tế","thô kệch","mịn màng","sần sùi","bóng loáng","mờ ảo","sáng chói","tối om","âm u","u ám","quang đãng","trong veo","đục ngầu","tinh khiết","thuần khiết","nguyên chất","hỗn tạp","đa dạng","phong phú","nghèo nàn","sung túc","đầy đủ","thiếu thốn","dư dả","chan hòa","hài hòa","cân đối","lệch lạc","ổn định","bất ổn","yên tĩnh","ồn ào","náo nhiệt","vắng vẻ","đông đúc","thưa thớt","san sát","rải rác","lác đác","tấp nập","nhộn nhịp"]

lines = set()

def add(h, a):
    lines.add(f"{h}|{a}")

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
    add("quả...", f"quả {w} to")
    add("quả...", f"quả {w} nhỏ")
    for c in mau_sac[:15]:
        add("quả...", f"quả {w} màu {c}")

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

for a in trai_cay:
    for b in mau_sac[:15]:
        add("quả...", f"quả {a} màu {b} chín")

for a in dong_vat:
    for b in hanh_dong:
        if len(a) + len(b) < 25:
            add("con...", f"con {a} đang {b}")

for a in do_vat:
    for b in vat_lieu:
        add("cái...", f"cái {a} làm bằng {b}")

for a in nghe_nghiep:
    for b in tinh_cam:
        add("người...", f"người {a} rất {b}")

WORDS = []
for line in sorted(lines):
    if "|" in line:
        hint, answer = line.split("|", 1)
        WORDS.append({"hint": hint.strip(), "answer": answer.strip()})

print(f"Da load {len(WORDS)} tu")
