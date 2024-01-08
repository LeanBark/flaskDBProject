from datetime import date

today = date.today()
year, month, day = today.year, today.month, today.day
year_list = [str(i) for i in range(1900, year + 1)]
month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
day_list = [str(i) if i > 9 else "0" + str(i) for i in range(1,32)]

print(year_list)
print(month_list)
print(day_list)

                        # <select class="form-select" name="sale-year" id="sale-year" required>
                        #     <option value="">Select Year</option>
                        #     {% for year in years %}
                        #     <option value="{{year}}">{{year}}</option>
                        #     {% endfor %}
                        # </select>

                        # <select class="form-select" name="sale-month" id="sale-month" required>
                        #     <option value="">Select Month</option>
                        #     {% for month in months %}
                        #     <option value="{{month}}">{{month}}</option>
                        #     {% endfor %}
                        # </select>

                        # <select class="form-select" name="sale-day" id="sale-day" required>
                        #     <option value="">Select Day</option>
                        #     {for day in valid_days %}
                        #     <option value="{{day}}">{{day}}</option>
                        #     {% endfor %}
                        # </select>
    # <script language="JavaScript">
    # document.addEventListener("DOMContentLoaded", () =>{
    #     document.getElementById("display-invoices").style.display = "block";
    #     document.getElementById("add-invoice-btn").style.display = "block";
    #     document.getElementById("add-invoice").style.display = "none";
    #     document.getElementById("edit-invoice").style.display = "none";
    # });

    # function displayController(situation){
    #     if(situation == "add"){
    #         document.getElementById("display-invoices").style.display = "none";
    #         document.getElementById("add-invoice-btn").style.display = "none";
    #         document.getElementById("add-invoice").style.display = "block";
    #         document.getElementById("edit-invoice").style.display = "none";
    #     }

    #     else if(situation == "edit"){
    #         document.getElementById("display-invoices").style.display = "none";
    #         document.getElementById("add-invoice-btn").style.display = "none";
    #         document.getElementById("add-invoice").style.display = "none";
    #         document.getElementById("edit-invoice").style.display = "block";
    #     }

    #     else {
    #         document.getElementById("display-invoices").style.display = "block";
    #         document.getElementById("add-invoice-btn").style.display = "block";
    #         document.getElementById("add-invoice").style.display = "none";
    #         document.getElementById("edit-invoice").style.display = "none";
    #     }
    # }

    # function addInvoice() {
    #     displayController('add');
    # }

    # function editInvoice() {
    #     displayController('edit');
    # }

    # function showInvoices() {
    #     displayController('');
    # }

    # </script>
                    # <div class="row">
                    #     <div class="col-5">        
                    #         <select class="form-select" name="menu-item-value" id="menu-item-value" required>
                    #             <option value="">Select Menu Item</option>
                    #             {% for item in menu %}
                    #             <option value="{{item.menu_itemID}}">{{item.name}}</option>
                    #             {% endfor %}
                    #         </select>
                    #     </div>
                    #     <div class="col-3">
                    #         <input class="form-control" type="number" name="quantity-sold" id="quantity-sold" placeholder="Quantity Value" required>
                    #     </div>
                    #     <div class="col-4">
                    #         <div class="input-group date" data-provide="datepicker-inline" data-date-format="yyyy-mm-dd">
                    #             <input type="date" class="form-control" placeholder="YYYY-MM-DD" required>
                    #             <div class="input-group-addon">
                    #                 <span class="glyphicon glyphicon-calendar"></span>
                    #             </div>
                    #         </div> 
                    #     </div>
                    # </div>
                    # <div class="row">
                    #     <div class=""d-grid gap-2 d-md-block">
                    #         <button class="btn btn-success" type="submit" name="Add Invoice" value="Add Invoice" id="Add Invoice">Add Invoice</button>
                    #         <input class="btn btn-danger" type="button" value="Cancel" onclick="showInvoices()">
                    #     </div>
                    # </div>
# .on("change", function(e) {
#             $("#sales-date").val($(e.currentTarget).val());
#         });
    