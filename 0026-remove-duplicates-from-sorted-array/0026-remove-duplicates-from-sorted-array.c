int removeDuplicates(int* nums, int numsSize) {
    int prev = nums[0];
    int count = 1;

    for(int i = 1; i < numsSize; i++){
        if (nums[i] != prev){
            count++;
            nums[count-1] = nums[i];
        }
        prev = nums[i];
    }
    return count;
}