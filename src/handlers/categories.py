from flask import request, jsonify
from src.models.category import Category

class CategoryHandler:
    @staticmethod
    def get_categories():
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 5))  

        # Get total count
        total_categories = Category.query.count()
        total_pages = (total_categories + limit - 1) // limit  

        # Fetch paginated categories
        categories = (Category.query
                      .order_by(Category.id.desc())
                      .offset((page - 1) * limit)
                      .limit(limit)
                      .all())

        # Convert to JSON response
        category_list = [{"id": c.id, "name": c.name, "image_url": c.image} for c in categories]

        # Pagination metadata
        pagination = {
            "current_page": page,
            "total_pages": total_pages,
            "next_page": page + 1 if page < total_pages else None
        }

        return jsonify({"categories": category_list, "pagination": pagination})
