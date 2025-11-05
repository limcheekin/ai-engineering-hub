import parlant.sdk as p

def show_defaults():
    # instantiate the built-in ProductionAuthorizationPolicy
    policy = p.ProductionAuthorizationPolicy()
    limiter = policy.default_limiter

    print("Limiter class:", type(limiter))
    # rate_limit_item_per_operation is a dict: Operation -> RateLimitItem
    rl_map = limiter.rate_limit_item_per_operation
    for op, item in rl_map.items():
        print(f"{op!r:40} -> {item!r}")

if __name__ == "__main__":
    show_defaults()
