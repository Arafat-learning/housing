from itemadapter import ItemAdapter


class WebscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Clear whitespace
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != "floor": # floor may not be a string and throw an error
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()

        # Convert number inputs from string to number
        # price
        try:
            value = adapter.get("price")
            adapter["price"] = int(value.replace("\xa0", ""))
        except:
            print("newly build price is not converted")
        # room count
        value = adapter.get("room_count")
        adapter["room_count"] = int(value[0])
        # area
        value = adapter.get("area")
        adapter["area"] = float(value.split()[0])



        return item
