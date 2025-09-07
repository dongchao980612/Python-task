import csv

def process_score_file(input_file, failed_file, ranked_file):
    """处理成绩文件，生成不及格学生文件和排序后的总分文件"""
    students = []
    with open(input_file, 'r', encoding='utf-8') as f:
        # 读取表头
        header = f.readline().strip()
        print("header = ",header)
        # 读取学生数据
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                student_id, name, score_a, score_b, score_c = parts
                # 转换成绩为整数
                try:
                    scores = [int(score_a), int(score_b), int(score_c)]
                    total = sum(scores)
                    students.append({
                        'id': student_id,
                        'name': name,
                        'scores': scores,
                        'total': total,
                        'failed': any(score < 60 for score in scores)
                    })
                except ValueError:
                    print(f"跳过无效行: {line}")
    
    # 生成failed.txt
    with open(failed_file, 'w', encoding='utf-8') as f:
        f.write(header + '\n')  # 写入表头
        for student in students:
            if student['failed']:
                f.write(f"{student['id']}\t{student['name']}\t{student['scores'][0]}\t{student['scores'][1]}\t{student['scores'][2]}\n")
    
    # 生成ranked.txt（按总分从高到低排序）
    with open(ranked_file, 'w', encoding='utf-8') as f:
        f.write("ID\tName\tTotal_Score\n")  # 写入新表头
        # 按总分降序排序
        sorted_students = sorted(students, key=lambda x: x['total'], reverse=True)
        for student in sorted_students:
            f.write(f"{student['id']}\t{student['name']}\t{student['total']}\n")


def process_price_file(input_file, up_file, down_file):
    """处理价格文件，生成涨价和降价产品文件"""
    products = []
    
    # 读取price.csv文件
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # 提取并转换价格数据
                goods = row['Goods']
                price_2018 = float(row['Price_2018'])
                price_2019 = float(row['Price_2019'])
                
                products.append({
                    'goods': goods,
                    'price_2018': price_2018,
                    'price_2019': price_2019,
                    'change': price_2019 - price_2018
                })
            except (ValueError, KeyError) as e:
                print(f"跳过无效行: {row}, 错误: {e}")
    
    # 生成up.csv（涨价产品）
    with open(up_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Goods', 'Price_2018', 'Price_2019'])  # 写入表头
        for product in products:
            if product['change'] > 0:
                writer.writerow([
                    product['goods'],
                    product['price_2018'],
                    product['price_2019']
                ])
    
    # 生成down.csv（降价产品）
    with open(down_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Goods', 'Price_2018', 'Price_2019'])  # 写入表头
        for product in products:
            if product['change'] < 0:
                writer.writerow([
                    product['goods'],
                    product['price_2018'],
                    product['price_2019']
                ])


if __name__ == "__main__":
    # 处理成绩文件
    process_score_file('score.txt', 'failed.txt', 'ranked.txt')
    print("成绩文件处理完成")
    
    # 处理价格文件
    process_price_file('price.csv', 'up.csv', 'down.csv')
    print("价格文件处理完成")
