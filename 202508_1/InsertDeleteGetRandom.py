import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []    # 실제값들을 담는 리스트
        self.val_to_index = {}  # 딕셔너리에 인덱스를 저장해두면 위치를 바로 알 수 있다..! 그때를 위한 딕셔너리

    def insert(self, val):
        if val in self.val_to_index:    # val이 있으면 False 반환
            return False
        self.val_to_index[val] = len(self.nums) # 없으면 nums의 끝에 추가하기
        self.nums.append(val)   # 딕셔너리에는 val: 인덱스를 저장
        return True

    def remove(self, val):
        if val not in self.val_to_index:    # 존재하지 않으면 False 반환
            return False

        # 삭제할 값의 인덱스
        idx = self.val_to_index[val]
        # 마지막 값
        last_val = self.nums[-1]

        # 마지막 값을 삭제할 위치로 옮김
        self.nums[idx] = last_val    # 삭제할 값을 리스트의 끝으로 옮기기
        self.val_to_index[last_val] = idx   # 딕셔너리 값 업데이트

        # 마지막 원소 삭제 및 딕셔너리 정리 -> 중간에서 값을 찾으면 시간이 오래 걸리기에 끝값이랑 교환해서 하면 시간 복잡도가 작아짐
        self.nums.pop()
        del self.val_to_index[val]  # 항목 삭제

        return True

    def getRandom(self):    # 랜덤으로 하나 선택
        return random.choice(self.nums)