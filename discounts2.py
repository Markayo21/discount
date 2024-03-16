def calculated_discount(price,discount_percent):

    """
      Calculates the final price after applying a discount (if applicable).

      Args:
          price: The original price of the item.
          discount_percent: The discount percentage (0 to 100).

      Returns:
          The final price after applying the discount, or the original price if the discount is less than 20%.
      """
    if discount_percent >=20:
        discount = price * discount_percent/100
        final_price = price - discount
        print(f"Final price after discount: ksh{final_price:.2f}")
        return final_price
    else : 
        final_price  = price
        print(f"No discount applied. Original price: ksh{final_price:.2f}")  # Print inside the function
        return final_price
price = float(input("Enter original price of item :"))
discount_percent = float(input ("Enter the discount percentage (0-100) :"))

final_price = calculated_discount(price,discount_percent)





